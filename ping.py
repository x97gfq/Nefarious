#ping using TCP/IP sockets - prompts user for IP address (e.g. 192.168.0.x)
#based on https://www.cybrary.it/blog/0p3n/ping-using-python-script/
import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server_ip = input('Enter server IP : ')
rep = os.system('ping ' + server_ip)
if rep == 0:
    print('server is up')
else:
    print('server is down')
    