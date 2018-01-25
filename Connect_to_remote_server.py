#!/usr/bin/env python
from sys import argv

if len(argv)>3 or len(argv)<2:
    print("USAGE: command #IP #PORT (Port is optional, port 22 will be used by default)")
    exit()

ip_port=[]
for i in range(1,len(argv)):
    ip_port.append(argv[i])

ip_port=tuple(ip_port)


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

def connect_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((str(ip),int(port)))
    if result == 0:
        return True
    else:
        return False

arguments=str(len(argv)-1)
connectisok = {
    '1': (ip_check(ip_port[0])),
    '2': (ip_check(ip_port[0]) and port_check(ip_port[1]))
}[arguments]

def con_wo_port(): print("Run connect_port(ip_port[0],'22') which is Run connect_port(%s,'22')") % (ip_port[0])

try:
    def con_w_port(): print("Run connect_port(ip_port[0],ip_port[1]) which is Run connect_port(%s,%s)") % (ip_port[0],ip_port[1])
except:
    pass

{
    '1': con_wo_port,
    '2': con_w_port
}[arguments]()