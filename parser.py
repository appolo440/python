f=open("server.log", "r")
line = f.readline()
while line:
	print ,	
	cutline = line.split()
	print (cutline[0])
	line = f.readline()
f.close;	