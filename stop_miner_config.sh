#!/bin/bash
echo Content-type: text/html
echo ""

kill -9 `ps -aux | grep 'python3 /var/www/html/eth_miner/config.py' | grep -v grep | awk '{print $2}'`
kill -9 `ps -aux | grep 'python3 /var/www/html/eth_miner/check_restart.py' | grep -v grep | awk '{print $2}'`


if [ $? == 0 ];
then 
    echo {"result":"successfully stop"}
else
    echo {"result":"failed to stop"}
fi
