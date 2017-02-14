# -*- coding: utf-8 -*-
import os, datetime

root = "/home/yakunin/"
diffsize = 3.0

os.system('touch ' + root + 'today.log')
os.system('touch ' + root + 'yestoday.log')

if os.path.exists(root + 'today.log'):
 os.system('mv ' + root + 'today.log ' + root + 'yestoday.log')

f = open(root + 'today.log', 'w')

for item in os.listdir(root):
  if not '.' in item:
   if os.path.isdir(os.path.join(root, item)):
    def get_size(start_path = root + item):
     total_size = 0
     for dirpath, dirnames, filenames in os.walk(start_path):
	for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
     return float(total_size)
    totals = round(get_size() / 1024 / 1024,1)
    f.write(str(totals) + ' ' + item + '\n')
f.close

today_array = []
f = open(root + 'today.log', 'r')
for line in f:
	today_array.append(line)
f.close()

yestoday_array = []
f = open(root + 'yestoday.log', 'r')
for line in f:
	yestoday_array.append(line)
f.close()

x = 0
diff_array = []

f = open(root + 'diff.log', 'w')
for lines in today_array:
 if today_array[x] == yestoday_array[x]:
   f.write(yestoday_array[x])
 else:
   f.write(today_array[x])
 x += 1
f.close()

# begin of report generation

f = open(root + 'diff.log', 'r')
print ('Находимся в: ' + root)

for line in f:
	L = line.strip()
	C = L.split()
	if diffsize > float(C[0]):
		print (str(diffsize) + '>' + C[0] + ' Нет	' + C[1])
	else:
		print (str(diffsize) + '<' + C[0] + ' Да	' + C[1])
f.close()