# -*- coding: utf-8 -*-

import subprocess
subprocess.call('wget -q http://xml.meteoservice.ru/export/gismeteo/point/37.xml', shell=True)

f = open ('37.xml', 'r')
line = f.readlines()

tempall = line[7]
print(tempall[22:24] + ' ' + tempall[31:33])

#wind = line[8]
#print('Ветер: ' + wind[23:24])

tempheat = line[11]
print(tempheat[25:28])

f.close()
subprocess.call('rm 37.xml', shell=True)