#!/usr/bin/python3

#import pyrcon
import json
import time
import requests


def get_latest_messages():
    GITHUB_URL=https://github.com/actionquake/servermessages/messages
    r = requests.get(GITHUB_URL, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)




server_groups = []
server_ports = {}
server_rcon = {}
messages = {}

## Load server info
with open('aq2servers.json', 'r') as f:
    servers = json.load(f)
    f.close
    for servergroup in servers["servers"]:
        server_groups = list(servers["servers"].keys())
        server_ports[servergroup] = servers["servers"][servergroup]["server_ports"]
        server_rcon[servergroup] = servers["servers"][servergroup]["rcon_passwords"]

## Load messages
with open('aq2messages.json', 'r') as f:
    messagelist = json.load(f)
    f.close
    for messagegroup in messagelist["servers"]:
        messages[messagegroup] = messagelist["servers"][messagegroup]

# print(server_groups)
# print(server_ports)
# print(server_rcon)
# print(messages)
# print(messages["aq2world-east"])

def sendMessage(message):
    for idx in range(len(server_ports)):
        conn = pyrcon.Q2RConnection("localhost", server_ports[idx], server_rcon[idx])
        cmd = conn.send(message)
        print(cmd)

message_list = []

for server in server_groups:
    for msg in range(len(messages[server])):
        message_list.append(messages[server][msg])


server_message = [server_groups, message_list]
server_message_iterator = [item[1] for item in server_message]

#print(message_list)

print(server_message)
#print(server_message_iterator)

## Simple loop
#while(True):
#for server_group in range(len(server_groups)):
    #print(server_groups)
    #print(server_groups[server_group])
    #print(messages[server_groups[server_group]][0])
    #print(messages[server_groups[server_group]][1])
    #print(zip(messages[server_groups[server_group]]))
    #for server, message in zip(messages[server_groups[server_group]],messages[server_groups[server_group]][msgcount]):
    #    print(server)
    #    print(message)
    #for msgcount in range(len(messages[server_groups[server_group]])):
    #    time.sleep(1)
    #    print(messages[server_groups[server_group]][msgcount])
