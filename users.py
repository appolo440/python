#!/usr/bin/python
import getpass, os

# Setting up path to sshd_config file.
sshd_file= "/home/yakunin/Work/programming/python/ssh/log"

# Don't edit any other parametrs here.
action = raw_input("action: ")
if action == "close":
	username = raw_input('username: ')
	userpass = getpass.getpass('password: ')
	remoteserver = raw_input('server: ')

	print ("Run command on remote server...")
	print ("Begin edit sshd_conf file.")

	os.system("sshpass -p " + userpass + " ssh " + username + "@" + remoteserver + " \" sed -i 's/^#DenyUsers appsuser,poo.*/DenyUsers appsuser,poo/g' " + sshd_file + " \" ")

	print ("Done.")
	print ("Just restart SSH server to apply changes...")

	os.system("/etc/init.d/ssh restart")

elif action == "open":
	username = raw_input('username: ')
	userpass = getpass.getpass('password: ')
	remoteserver = raw_input('server: ')

	print ("Run command on remote server...")
	print ("Begin edit sshd_config file.")

	os.system("sshpass -p " + userpass + " ssh " + username + "@" + remoteserver + " \" sed -i 's/^DenyUsers appsuser,poo.*/#DenyUsers appsuser,poo/g' " + sshd_file + " \" ")

	print ("Done.")
	print ("Just restart SSH server to apply changes...")

	os.system("/etc/init.d/ssh restart")
else:
	print("Bad action, or is empty, please use: open or close")
	print("Quit...")
