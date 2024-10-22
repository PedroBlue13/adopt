#!/bin/bash
SERVER_PATH="/home/ubuntu/dev_work/manage.py runserver" 



python3 $SERVER_PATH 9000 > server_web.log 2>&1 &