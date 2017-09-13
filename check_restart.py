#!/usr/bin/env python3
#from mining import application
#from cherrypy import wsgiserver
import sys
import json
import subprocess
import cgitb


print("Content-type: text/html\n")

cgitb.enable()

PATH = '/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/config_save.txt'
fhandler = open(PATH, 'rt')

result = json.loads(fhandler.read())


if 'restart' in result.values():
   # server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8080), application)
   # server.start()
    subprocess.Popen(['sudo /opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/ethdcrminer64'], shell=True)
else:
    sys.exit()

fhandler.close()
