# -*- coding: utf-8 -*-

import subprocess
import xml.dom.minidom
import time

time.sleep(1)

subprocess.call('wget -q http://xml.meteoservice.ru/export/gismeteo/point/37.xml', shell=True)

dom = xml.dom.minidom.parse("37.xml");
dom.normalize()

node1 = dom.getElementsByTagName("HEAT")[0]
node2 = dom.getElementsByTagName("TEMPERATURE")[0]

a = node1.getAttribute("min")
b = node1.getAttribute("max")

c = node2.getAttribute("min")
d = node2.getAttribute("max")

if a >= b:
 heat = a
else:
 heat = b

if c >= d:
 temper = c
else:
 temper = d

print heat
print temper

subprocess.call('rm 37.xml', shell=True)