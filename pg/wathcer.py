#!/usr/bin/python3.5
import socket
import threading
import os

class Clicker(object):
        prev_button = None
        def click(self, button=None):
                if button != self.prev_button:
                        self.prev_button = button
                        print(button)

def CUSTOMPORT():
        threading.Timer(0.5, CUSTOMPORT).start()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("192.168.1.10",80))
        if result == 0:
                clc.click("Service is up")
        else:
                clc.click("Service is down")
                os.popen('service nginx start')

#       proc = os.popen('ps uax').read()
#       if proc.find("postgres") == -1:
#               clc.click("Service is down")
#               os.popen('service postgresql start')
#       else:
#               clc.click("Service is up")

clc = Clicker()
CUSTOMPORT()
