#!/usr/bin/python

import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 0
BUFFER_SIZE = 16384

LOGFILE = open('access.log', 'w')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

while 10:

	conn, addr = s.accept()
	conn.settimeout(60)

	try:
		while 10:
			data = conn.recv(BUFFER_SIZE)
			udata = data.decode("utf-8")
			if not data: break
			LOGFILE.write(udata,)
			print udata, #echo for debug
	except:
		pass

	LOGFILE.close
	conn.close()
