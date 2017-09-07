#!/usr/bin/env python3
import json
import cgitb

print("Content-type: text/html\n")
cgitb.enable()
fhandler = open("/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/config.txt", "rt")
value = fhandler.read().split('\n')

result = {}
for i in value:
	con = i.split(' ')
	result[con[0]] = con[1]

fhandler.close()

fhand = open("/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/config_save.txt", "rt")
args = json.loads(fhand.read())
fhand.close()

result = dict(result, **args)

print(json.dumps(result))
