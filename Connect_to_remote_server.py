#!/usr/bin/env python
from sys import argv

ip=argv[1]

def ip_check(ip2ch):
    ip_split = ip2ch.split('.')
    if ip_split[3]=='0' or ip_split[0]=='0' or not len(filter(lambda x:int(x) <= 255 and int(x) >= 0 , ip_split)) == 4 :
        return False
    return True