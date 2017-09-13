#!/bin/bash
echo Content-type: text/html
echo ""

kill -9 `ps aux | grep '/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/ethdcrminer64' | awk {'print $2'}`

