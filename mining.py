#!/usr/bin/env python3
#encoding: utf-8

import subprocess
from cherrypy import wsgiserver

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    proc = subprocess.Popen(['sudo /opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/ethdcrminer64'], shell=True, stdout=subprocess.PIPE)

    line = proc.stdout.readline()
    while line:
        yield line
        line = proc.stdout.readline()

if __name__ == '__main__':
    server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8080), application)
    server.start()
