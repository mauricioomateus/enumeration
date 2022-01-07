#!/usr/bin/python

import socket,sys,re

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],22))

banner = tcp.recv(1024)
banner = re.sub(b"\r\n",b"",banner)
print (banner)
