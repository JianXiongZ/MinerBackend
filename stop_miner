#!/bin/bash
echo Content-type: text/html
echo ""

kill -9 `ps -aux | grep '/home/canaan/eth_miner/ethdcrminer64' | grep -v grep | awk '{print $2}'`

if [ $? == 0 ];
then 
    echo {"result":"successfully stop"}
else
    echo {"result":"failed to stop"}
fi
