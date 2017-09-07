#!/bin/bash
echo Content-type: text/html
echo ""

arg1=`ps aux | grep 'python3 /var/www/html/eth_miner/config.py' | grep -v grep | awk '{print $2}'`
arg2=`ps aux | grep 'wget "http://127.0.0.1/eth_miner/check_restart.py"' | grep -v grep | awk '{print $2}'`


if [ -n $arg1 ];
  then
    /var/www/html/eth_miner/stop_miner_config.sh
fi
if [ -n $arg2 ];
  then 
    sudo /var/www/html/eth_miner/stop_miner_restart.sh
fi
 
if [ $? == 0 ];
then 
    echo {"result":"successfully stop"}
else
    echo {"result":"failed to stop"}
fi
