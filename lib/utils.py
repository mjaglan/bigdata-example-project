import base64
import hashlib
import nclient
import subprocess as sub
import sys

# http://stackoverflow.com/a/6682934
def fingerprint_from_string(line):
    key = base64.b64decode(line.strip().split()[1].encode('ascii'))
    fp_plain = hashlib.md5(key).hexdigest()
    return ':'.join(a+b for a,b in zip(fp_plain[::2], fp_plain[1::2]))

def list_of_fingerprints():
    res = []
    nova = nclient.auth()
    klist = nova.keypairs.list() 
    for key in klist:
        res.append(key.fingerprint)
    return res

def list_of_servers():
    nova = nclient.auth()
    return nova.servers.list() 

def find_server(name):
    slist = list_of_servers()
    for server in slist:
        if server.name == name:
            return server
    return False

def get_floating_ip(server):
    if not server:
        return False
    for i in server.addresses:
        for net in server.addresses[i]:
            if net['OS-EXT-IPS:type'] == 'floating':
                return net['addr']
    return False

def call_ssh(ip, login="ubuntu", cmd="uname -s"):

    p = sub.Popen(["ssh", "-l" , login,  ip, cmd], shell=False, stdout=sub.PIPE,
            stderr=sub.PIPE) 
    stdout, stderr = p.communicate()
    return stdout, stderr

