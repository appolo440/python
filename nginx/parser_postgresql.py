#!/usr/bin/python

import re
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

filename = '/var/log/nginx/access.log'
regex = r"^(?P<ipaddress>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})(.+\[.+\].)(\")(?P<method>\S{1,5}).(?P<request>\S+).(\S+).(?P<response>\d{1,4}).(?P<bytes>\d+).(\S+).(\")(?P<useragent>[^\"]+)..(?P<request_length>\d+).(?P<request_time>\d+\.?\d*)(\s.)(?P<requst_body>[^\"]+)"

f = subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
	line = f.stdout.readline()
	m = re.finditer(regex, line)
	for r in m:
		ip_addr = r.group('ipaddress')
		method = r.group('method')
		request = r.group('request')
		response = r.group('response')
		bytes = r.group('bytes')
		request_length = r.group('request_length')
		request_time =	r.group('request_time')
		requst_body = r.group('requst_body')
		useragent = r.group('useragent')

		# print (ip_addr + '\t' + method + '\t' + response + '\t' + bytes + '\t' +  request_length + '\t' + request_time + '\t' +request) # STRING FOR DEBUG

		sql = "INSERT INTO logs(time, ip_addr, request, response, bytes, useragent) VALUES (%s, %s, %s, %s, %s, %s);"
		data = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip_addr, request, response, bytes, useragent)
		cursor.execute(sql, data)
		conn.commit()
