#!/usr/bin/python

import socket,sys

if len(sys.argv) != 3:
        print "Modo de uso: python3 enumsmtp.py IP user"
        sys.exit(0)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],25))

banner = tcp.recv(1024)
print (banner)

tcp.sendall(b'VRFY '+sys.argv[2]+'\r\n')
usr = tcp.recv(1024)
print (user)
