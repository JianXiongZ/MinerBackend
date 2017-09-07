#!/bin/bash
echo Content-type: text/html
echo ""

kill -9 `ps -aux | grep 'wget http://127.0.0.1/eth_miner/check_restart.py' | grep -v grep | awk '{print $2}'`

