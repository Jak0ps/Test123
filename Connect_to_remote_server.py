#!/usr/bin/env python
from sys import argv

ip=argv[1]
port=argv[2]

def ip_check(ip2ch):
    ip_split = ip2ch.split('.')
    if ip_split[3]=='0' or ip_split[0]=='0' or not len(filter(lambda x:int(x)<=255 and int(x)>=0,ip_split))==4 :
        return False
    return True

def port_check(port2ch):
    if int(port2ch)>0 and int(port2ch)<=65535:
        return True
    else:
        return False

arguments=str(len(argv)-1)
connectisok = {
    '1': (ip_check(ip)),
    '2': (ip_check(ip) and port_check(port))
}[arguments]

def con_wo_port(): print('1st func')

def con_w_port(): print('2nd func')

{
'1': con_wo_port,
'2': con_w_port
}[arguments]()
