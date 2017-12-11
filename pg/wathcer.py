#!/usr/bin/python3.4

import socket
import threading
import datetime
import os

PG_STATUS = None

CURRENT_DATE = datetime.datetime.now()
print (CURRENT_DATE.strftime("%d.%m.%Y %H:%M:%S") + " Start watch on service")

def CUSTOMPORT():
	global PG_STATUS
	CURRENT_DATE = datetime.datetime.now()

	threading.Timer(0.5, CUSTOMPORT).start()
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	PG_CURRENT = sock.connect_ex(("localhost",22))

	if PG_STATUS != PG_CURRENT:
		if PG_CURRENT == 0:
			print (CURRENT_DATE.strftime("%d.%m.%Y %H:%M:%S") + " Service is up")
		else:
			print (CURRENT_DATE.strftime("%d.%m.%Y %H:%M:%S") + " Service is down")

			print (CURRENT_DATE.strftime("%d.%m.%Y %H:%M:%S") + " Try to restart service")
			os.popen('sudo service ssh restart')

	PG_STATUS = PG_CURRENT

CUSTOMPORT()
