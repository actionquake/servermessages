#!/usr/bin/python3

#import pyrcon
import json
import time
from tokenize import Name
import requests
import gnupg 
import io
gpg = gnupg.GPG(gnupghome="/Users/dino/.gnupg")

PUB_GPG="0xA6C60ABC636EF79B"
GIT_API="https://api.github.com/repos/actionquake/servermessages/git/trees/main?recursive=1"
GIT_URL="https://github.com/actionquake/servermessages/srv"
GIT_RAW="https://raw.githubusercontent.com/actionquake/servermessages/main"

def get_latest_server_files(filetype):
    if filetype not in ["msg", "rcon"]:
        raise NameError("Function param must be one of msg or rcon")

    r = requests.get(GIT_API)
    get_json = json.loads(r.content)
    get_json_paths = get_json["tree"]    
    file_list = []
    
    for filepath in get_json_paths:
        if (filepath["path"]).endswith(filetype):
            file_list.append(filepath["path"])
    return file_list

def decrypt_rcon(rcon_file):
    with open('aq2rcon.asc') as kfile:
        key = kfile.read()
        gpg.import_keys(key)

    rcon_file_path = GIT_RAW + "/srv/" + rcon_file
    response = requests.get(rcon_file_path)
    if response.status_code != 200:
        raise ValueError("rcon file not found: " + rcon_file)
    encrypted_file = response.content
    decrypt_file = gpg.decrypt(encrypted_file)

    decrypted_bytes = decrypt_file.data
    rcon_password = decrypted_bytes.decode("utf-8")
    return rcon_password


server_messages = {}
def get_server_messages():
    msgfiles = get_latest_server_files("msg")

    filenames = []
    for file in msgfiles:
        filepath = file.split('/', 1)
        filenames.append(filepath[1])

    for msg_file in filenames:
        server_name = msg_file.split('.', 1)
        response = requests.get(GIT_RAW + "/msgs/" + msg_file)
        content = response.content.decode("utf-8")
        print(content)
        print(type(content))
        server_messages[server_name[0]] = content
    

#decrypt_rcon("aq2world-west.rcon.gpg")
get_server_messages()

print(server_messages)


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
