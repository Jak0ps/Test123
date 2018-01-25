#!/usr/bin/env python
#start in background #nohup /scripts/file.py &


from os.path import getmtime
from time import sleep

acctime = getmtime("/scripts/test.py") - 1
logf = open("/tmp/test.txt","w")

while True:
    try:
        if getmtime("/scripts/test.py") > acctime:
            acctime = getmtime("/scripts/test.py")
            with open("/scripts/test.py",'r') as f:
                for line in f:
                    logf.write(line)
    except Exception as e:
        logf.write(str(e))
        logf.close()
        break
    sleep(5)