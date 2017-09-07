#!/usr/bin/env python3
#encoding: utf-8

import cgi, cgitb
import sys
import json

from mining import application
from cherrypy import wsgiserver


print("Content-type: text/html")
print("")

form = cgi.FieldStorage()


PATH_SAVE = '/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/config_save.txt'
PATH = '/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/config.txt'

def write_data(data):
    f = open(PATH_SAVE,'w+') 
    f.write(json.dumps(data))
    f.close()

if 'config_mining' in form:
    value = form.getvalue('config_mining')
    args = value.split(',')
    mining_pool = args.pop(0)
    du_mining_pool = args.pop(-1)

    fhandler = open(PATH, 'wt')

    for i in args:
        if len(i) == 0:
            print(json.dumps("non_input"))
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

    f=open(PATH_SAVE,'r')
    fd  = f.read()
    if fd == '':
        con = {}
    else:
    	con = json.loads(fd)
    
    con["onlypool"]=mining_pool
    con["dualpool"]=du_mining_pool
    
    f.close()
          
    write_data(con) 

    server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8080), application)
    server.start()

elif 'config_save' in form:
    config_list = form.getvalue('config_save')
    args = config_list.split(',')
    for j in args:
        if len(j) == 0:
            print(json.dumps("no_name_password"))
            sys.exit()

    f=open(PATH_SAVE,'r')
    fd  = f.read()
    if fd == '':
        con = {}
    else:
    	con = json.loads(fd)
    if len(args) == 1:
    	con["ifrestart"]=args[0]
    elif len(args) == 2:
    	con["username"]=args[0]
    	con["password"]=args[1]
    else:
    	con["ifrestart"]=args[0]
    	con["username"]=args[1]
    	con["password"]=args[2]
    
    f.close()
          
    write_data(con)

print(json.dumps({"config_save":"successed"}))

