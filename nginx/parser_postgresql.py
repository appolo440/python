#!/usr/bin/python

import psycopg2
import subprocess
import datetime

HOSTNAME = ""
DBNAME = ""
USERNAME = ""
PASSWORD = ""

conn_string = "host='" + HOSTNAME + "' dbname='" + DBNAME +"' user='" + USERNAME + "' password='" + PASSWORD + "'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

filename = 'access.log'
f = subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
	line = f.stdout.readline()
	sline = line.split(' ')

	# IP ADDRESS
	ip = sline[0]

	# REQUEST
	req = sline[6]

	# SERVER RESPONSE
	resp = sline[8]

	# REQUEST SIZE BYTES
	rsize = sline[9]

	# USER AGENT
	agentline = line.split('"')
	ua = agentline[5]

	# REQUEST BODY
	requestline = line.split('"')
	rbody = requestline[7]

	#print(ip + '\t\t' + req + '\t\t' + resp + '\t\t' + rsize + '\t\t' + ua + '\t' + rbody) # STRING FOR DEBUG

	sql = "INSERT INTO logs(time, ip, request, response, bytes, ua) VALUES (%s, %s, %s, %s, %s, %s);"
	data = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, req, resp, rsize, ua)
	cursor.execute(sql, data)
	conn.commit()
