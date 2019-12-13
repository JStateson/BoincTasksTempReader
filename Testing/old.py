#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket
import os


port=31417
hostname=os.uname()[1]
host=""  # this seems to work better than 127.0.0.1


strHeader="<TThrottle><HN:" + hostname + ">"
strPrefix= strHeader + "<PV 7.72><AC 1><TC 22><TG 31>"
strUNK="<NA 2><DC 100><DG 100>"
strENDING="<GT0 31.0><RS?G_jWJt><AA1><SC77><SG80><XC100><MC2><TThrottle>"
mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
conn, addr=mySocket.accept()
print ("Connection Established: " + str(addr))

r_dev = os.popen("sensors | grep Core").read().splitlines()
s_cpu = ""
n_cpu = 0

for l in r_dev :
	a = l.split("+") 
	b = a[1].split(".")
	c = b[0]
	s_cpu = s_cpu + "<CT" + str(n_cpu) + " " + c + ">" 
	n_cpu = n_cpu + 1

r_dev = os.popen('nvidia-smi -q -d  TEMPERATURE | grep  "GPU Current Temp"').read().splitlines()
s_nv = ""
nv = 0
for l in r_dev :
	a = l.split()
	nv = nv + 1   # starts with 1 not 0
	s_nv = s_nv + "<NV" + str(nv) + " " + a[4] + ">"

r_dev = os.popen('sensors | grep "hyst "').read().splitlines()
s_ati = ""
for l in r_dev :
	a = l.split()
	print(a)

strOUT= strPrefix + s_ati + s_nv + strUNK + s_cpu + strENDING

while True :
	data = conn.recv(1024).decode()
	print("from boinctasks: " + str(data) + " of length " + str(len(data)))
	if not data :
		break
	conn.send(strOUT.encode())
	print("ATI   ", s_ati)
	print("NVidia", s_nv)
	print("CPU   ", s_cpu)
	print("Prefix", strPrefix)
	print("strUNK", strUNK)
	print("ENDING", strENDING)
conn.close


