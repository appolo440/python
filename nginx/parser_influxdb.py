#!/usr/bin/python

import subprocess
import datetime
from influxdb import InfluxDBClient

filename = 'access.log'
f = subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
	line = f.stdout.readline()
	sline = line.split(' ')

	# IP ADDRESS
	ip_address = sline[0]

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
	
	client = InfluxDBClient('localhost', '8086', 'influx', 'influx', 'nginx')
	client.write(['ip,tag=' + ip_address +' ip_address="' + ip_address + '"'],{'db':'nginx'},204,'line')

