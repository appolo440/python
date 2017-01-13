from optparse import OptionParser
from sys import argv
from os.path import abspath, dirname
 
parser = OptionParser()
 
parser.add_option('-s', '--silent', dest='silent', action='store_true', default=False, help="don't make sound")
parser.add_option('-v', '--version', dest='version', action='store_true', default=False, help="show version")
 
options, args = parser.parse_args()
 
if options.silent:
    print('Silent flag is set')
    if options.version:
	print('Version 1.0')
    else:
	quit()
else:
	if options.version:
		print('Version 1.0')
	else:
		print ('Program run and over this no args.')
    
 
#print('Script is launched from dir:', dirname(abspath(argv[0])))
 
if args:
    print('The rest args:', args)