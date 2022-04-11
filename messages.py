#!/usr/bin/python3

#import pyrcon
import json
import time
import requests

GIT_API="https://api.github.com/repos/actionquake/servermessages/git/trees/main?recursive=1"
GIT_URL="https://github.com/actionquake/servermessages/messages"
GIT_RAW="https://raw.githubusercontent.com/actionquake/servermessages/main/messages/"

def get_latest_server_files():
    #r = requests.get(GIT_API)
    #get_json = json.loads(r.content)
    get_json = [{'path': '.gitignore', 'mode': '100644', 'type': 'blob', 'sha': '94a2dd146a22340832c88013e9fe92663bb9f2cc', 'size': 6, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/94a2dd146a22340832c88013e9fe92663bb9f2cc'}, {'path': 'Dockerfile', 'mode': '100644', 'type': 'blob', 'sha': '6eedf16cfc0b49e7a90e504a833355d947b8555c', 'size': 91, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/6eedf16cfc0b49e7a90e504a833355d947b8555c'}, {'path': 'README.md', 'mode': '100644', 'type': 'blob', 'sha': 'aa1c1a21e93dc21cced77f706d1df459837fd3ac', 'size': 68, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/aa1c1a21e93dc21cced77f706d1df459837fd3ac'}, {'path': 'messages.py', 'mode': '100644', 'type': 'blob', 'sha': 'd7e7c218faad84cd263dc412ee2b445ff70b91c9', 'size': 2228, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/d7e7c218faad84cd263dc412ee2b445ff70b91c9'}, {'path': 'messages', 'mode': '040000', 'type': 'tree', 'sha': '03bd09f6a408ed6448b91461d5e86a4b6da24137', 'url': 'https://api.github.com/repos/actionquake/servermessages/git/trees/03bd09f6a408ed6448b91461d5e86a4b6da24137'}, {'path': 'messages/aq2world-east', 'mode': '100644', 'type': 'blob', 'sha': '75a08c5ae1376682abf8692a70d8f41847e59ff9', 'size': 85, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/75a08c5ae1376682abf8692a70d8f41847e59ff9'}, {'path': 'messages/aq2world-west', 'mode': '100644', 'type': 'blob', 'sha': 'cff0c1451e9b9989285bf8fa6642c47adec82ede', 'size': 85, 'url': 'https://api.github.com/repos/actionquake/servermessages/git/blobs/cff0c1451e9b9989285bf8fa6642c47adec82ede'}]
    for filepath in get_json:
        print(filepath["path"])

def get_latest_messages():
    
    r = requests.get(GIT_URL, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)



get_latest_server_files()

# server_groups = []
# server_ports = {}
# server_rcon = {}
# messages = {}

# ## Load server info
# with open('aq2servers.json', 'r') as f:
#     servers = json.load(f)
#     f.close
#     for servergroup in servers["servers"]:
#         server_groups = list(servers["servers"].keys())
#         server_ports[servergroup] = servers["servers"][servergroup]["server_ports"]
#         server_rcon[servergroup] = servers["servers"][servergroup]["rcon_passwords"]

# ## Load messages
# with open('aq2messages.json', 'r') as f:
#     messagelist = json.load(f)
#     f.close
#     for messagegroup in messagelist["servers"]:
#         messages[messagegroup] = messagelist["servers"][messagegroup]

# print(server_groups)
# print(server_ports)
# print(server_rcon)
# print(messages)
# print(messages["aq2world-east"])

# def sendMessage(message):
#     for idx in range(len(server_ports)):
#         conn = pyrcon.Q2RConnection("localhost", server_ports[idx], server_rcon[idx])
#         cmd = conn.send(message)
#         print(cmd)
