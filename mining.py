#!/usr/bin/env python3
#encoding: utf-8

import cgi, cgitb
#import json
import sys
import subprocess
import time 

form = cgi.FieldStorage()
value = form.getvalue('config')

args = value.split(',')
PATH = '/home/jianxiong/eth_miner/config.txt'


print("Content-type: text/html\n")

fhandler = open(PATH, 'wt')

for i in args:
    if len(i) == 0:
        print("non_input")
        sys.exit()

if len(args) == 3:
    fhandler.write('-epool ' + args[0] + '\n-ewal ' + args[1] + '\n-epsw ' + args[2] + '\n-mode 1')
elif len(args) == 4:
    fhandler.write('-epool ' + args[0] + '\n-ewal ' + args[1] + '\n-epsw ' + args[2] + '\n-eworker ' + args[3] +'\n-mode 1')
elif len(args) == 6:
    fhandler.write('-epool ' + args[0] + '\n-ewal ' + args[1] + '\n-epsw ' + args[2] + '\n-dpool ' + args[3] + '\n-dwal ' + args[4] + '\n-dpasw ' + args[5])
elif len(args) == 7:
    fhandler.write('-epool ' + args[0] + '\n-ewal ' + args[1] + '\n-epsw ' + args[2] + '\n-eworker ' + args[3] + '\n-dpool ' + args[4] + '\n-dwal ' + args[5] + '\n-dpasw ' + args[6])

fhandler.close()


result = subprocess.Popen('/var/www/html/eth_test/test.sh', stdout=subprocess.PIPE)

sys.stdout.write("Transfer-Encoding: chunked\r\n")
sys.stdout.write("Content-Type: text/html\r\n")

def chunk(msg=""): #why????
	return "\r\n%X\r\n%s" % ( len( msg ) , msg )

while True:
	time.sleep(.1)
	line = result.stdout.readline()
	if line:
		sys.stdout.write(chunk(line.decode('utf-8')))
		sys.stdout.flush()
	else:
		break
