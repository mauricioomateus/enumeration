#!/usr/bin/python

import socket

#se conectadno no serviço
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("192.168.0.106",21))
print ("Conectando ao servidor...")

#capturando o banner
banner = tcp.recv(1024)
print (banner)

#enviando usuario para o protocolo
print ("Enviando usuario...")
tcp.sendall(b'USER ftp\r\n')
user = tcp.recv(1024)
#print (user)

#enviando senha para o protocolo
print ("Enviando a senha...")
tcp.sendall(b'PASS ftp\r\n')
pw = tcp.recv(1024)
#print (pw)

print ("Enviando comando HELP")
tcp.sendall(b'pass\r\n')
tcp.sendall(b'ls -la\r\n')
cmd = tcp.recv(2048)
print (cmd)
