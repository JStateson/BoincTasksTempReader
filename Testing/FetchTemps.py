#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket
import os


port=31417
hostname=os.uname()[1]
host=""  # this seems to work better than 127.0.0.1

# AC is active
# TC is max temp of cpu
# TG is max temp of gpu (what about nv and at and intel)
# NA is number of ati cards
# NV is number of nvidia cards
strHeader="<TThrottle><HN:" + hostname + ">"
strPrefix= strHeader + "<PV 7.72><AC 0>"  #<TC 22><TG 31>"
# %100 for cpu and gpu
# the nvidia values can fbe found in nvidia-smi if useful
strPCT="<DC 100><DG 100>"
strENDING="<RS?G_jWJt><AA1><SC77><SG80><XC100><MC2><TThrottle>"

mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
conn, addr=mySocket.accept()
print ("Connection Established: " + str(addr))

r_dev = os.popen("sensors | grep Core").read().splitlines()
s_cpu = ""
n_cpu = 0
m_cpu = 0.0
for l in r_dev :
	a = l.split("+") 
	b = a[1].split(".")
	c = b[0]
	if float(c) > m_cpu :
		m_cpu = float(c)
	s_cpu = s_cpu + "<CT" + str(n_cpu) + " " + c + ">" 
	n_cpu = n_cpu + 1
hdr_out = "<TC " + "{:4.1f}".format(m_cpu) + ">"
print("max CPU temp ", m_cpu)
print("CPU temps ",s_cpu)


r_dev = os.popen('nvidia-smi -q -d  TEMPERATURE | grep  "GPU Current Temp"').read().splitlines()
s_nv = ""
s_m_nv = ""
n_nv = 0
m_nv = 0.0
for l in r_dev :
	a = l.split()
	s_nv = s_nv + "<GT" + str(n_nv) + " " + a[4] + ">"
	if float(a[4]) > m_nv :
		m_nv = float(a[4])
	n_nv = n_nv + 1
if n_nv > 0 :
	s_m_nv = "<TG " + "{:4.1f}".format(m_nv) + ">"
	print("max NVidia temp ",s_m_nv)
	print("NV temps ",s_nv)

h_nv = "<NV " + str(n_nv) + ">"
hdr_out = hdr_out + s_m_nv + h_nv

r_dev = os.popen('sensors | grep "hyst "').read().splitlines()
s_ati = ""
for l in r_dev :
	a = l.split()
	print(a)
h_ati = "<NA 0>"
hdr_out = hdr_out + h_ati

strOUT= strPrefix + hdr_out + strPCT + s_cpu + s_nv + strENDING

while True :
	data = conn.recv(1024).decode()
	print("from boinctasks: " + str(data) + " of length " + str(len(data)))
	if not data :
		break
	conn.send(strOUT.encode())
	print("sent: ",strOUT)
conn.close


