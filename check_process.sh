#!/bin/bash
echo Content-type: text/html 
echo ""
arg=`ps aux | grep '/opt/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner/ethdcrminer64' | wc -l`
if [ $arg -le 1 ];
    then 
	    echo '{"status":"not_mining"}'
else
	echo '{"status":"is_mining"}'
fi
