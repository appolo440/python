#!/usr/bin/python

import socket
import subprocess

TCP_IP = '0.0.0.0'
TCP_PORT = 0
BUFFER_SIZE = 16384
FILENAME = '/var/log/nginx/access.log'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

f = subprocess.Popen(['tail', '-f', FILENAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
	line = f.stdout.readline()
	uline = line.encode("utf-8")
	s.send(uline,)
else:
	s.close()
