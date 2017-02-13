# -*- coding: utf-8 -*-
import os

# Присваиваем массиву нулевое значение
dir_path = '/test/'
a = []

# Проходим по всем каталогам и файлам начиная от указанного до конца, выбираем только каталоги без файлов
# собираем размер всех файлов и каталогов и помещаем в маасив gbsize, переводим из байтов в мегабайты, если нужно
# перевести в гибабайты, добавляем ещё одно значение / 1024.


for root, dirs, files in os.walk(dir_path):
	for dirname in dirs:
		seldir = os.path.join(root,dirname)
		import functools as F
		def collect_files(files, dirname, fnames):
			files += map(F.partial(os.path.join, dirname), fnames)
		files = []
		os.path.walk(seldir, collect_files, files)
		total_size = float(sum(map(os.path.getsize, files)))
		gbsize = total_size / 1024 / 1024

		#print ("size: " + str(round(gbsize,1)) + "Gb")
		#dir_total = (round(gbsize,1))
		#print dir_total
		a.append(round(gbsize,1))
		
if os.path.exists(dir_path + 'today.log'):
# Записываем полученные данные массива в файл, предварительно преобразовав массив в строку.
	f = open(dir_path + 'yestoday.log', 'w')
	for s in a:
		st = s;
		f.write(str(st) + '\n')
	f.close()
else:
	f = open(dir_path + 'today.log', 'w')
	for s in a:
		st = s;
		f.write(str(st) + '\n')
	f.close()

# Задаем численность больше которой критерий будет считаться измененным, и обнуляем массив с данными
size_pointer = 15.2
today_array = []
yestoday_array = []

# Открываем файл для чтения и забираем данные в новый маассив для сравнения.
f = open (dir_path + 'today.log', 'r')
for line in f:
	today_array.append(float(line,))
f.close()

f = open (dir_path + 'yestoday.log', 'r')
for line in f:
	yestoday_array.append(float(line,))
f.close()


# Задаем первый индекс массива в 0, далее при цикле увеличиваем счетчик массива на +1 при каждом переходе
# Преобразоввываем полученное число массива в значение с точкой и сравниваем его с переменной <<a>>, если
# значение <<а>> больше чем ячейка массива, то выводим знак больше, в противном случае меньше.

#x = 0
#for line in b:
#	if a > float(b[x]):
#		print str(a) + ' больше ' + str((b[x]))
#	else:
#		print str(a) + ' меньше ' + str((b[x]))
#	x += 1