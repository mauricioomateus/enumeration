#!/usr/bin/python

import socket,sys,re

if len(sys.argv) != 2:
        print "Modo de uso: python3 enumsmtp.py IP"
        sys.exit(0) 

#abrir um aquivo com uma lista de usuarios
file = open("lista.txt") 
for linha in file:  
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((sys.argv[1],25))
        banner = tcp.recv(1024)
        #print (banner)
        
        tcp.sendall(b'VRFY '+linha)
        usr = tcp.recv(1024)
                #buscando por '252'
                if re.search("252",user):
                        print ("Usaurio encontrado: "+user).strip("252 2.0.0")
