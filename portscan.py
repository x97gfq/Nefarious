#simple port scanner
#based on https://pythonprogramming.net/python-port-scanner-sockets/
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('What IP Address to scan?: ')

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False

print('Scanning ' + target + ':')

for x in range(86):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')
