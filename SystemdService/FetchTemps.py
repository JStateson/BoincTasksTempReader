#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  s_ string, n_ numeric , r_ raw values, h_ header of string under construction,  m_ max value (numeric)


import time
import socket
import os
import random
import string
import signal
import sys

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

strRND7 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(7)])
# AA will be marked as inactive, max and min of CPU not neeeded (XC, MC) 
# probably could put average core temp into SC  but not useful and not sure what it is
#   same for SG. 
strENDING="<RS" + strRND7 + "><AA0><SC77><SG80><XC100><MC2><TThrottle>"

# sleep here to avoid problems when problems at exit
time.sleep(10)

mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
conn, addr=mySocket.accept()
#print ("Connection Established: " + str(addr))


# was a count of nvidia boards passed to us?
n_argCNT = len(sys.argv) - 1
n_NV_cnt  = 0
n_ATI_cxnt = 0

if n_argCNT != 0 :
	n_NV_cnt = int(sys.argv[1])
	n_ATI_cnt = int(sys.argv[2])
#	print("Expecting NV:", n_NV_cnt)
#	print("Expecting ATI:", n_ATI_cnt)

# get CPU info first
r_dev = os.popen("sensors | grep Core").read().splitlines()
s_cpu = ""
n_cpu = 0
m_cpu = 0.0
hdr_out = ""
gpu_temps = ""

for l in r_dev :
	a = l.split("+")
	b = a[1].split(".")
	c = b[0]
	if float(c) > m_cpu :
		m_cpu = float(c)
	s_cpu = s_cpu + "<CT" + str(n_cpu) + " " + c + ">" 
	n_cpu = n_cpu + 1
hdr_out = "<TC " + "{:4.1f}".format(m_cpu) + ">"
#print("max CPU temp ", m_cpu)
#print("CPU temps ",s_cpu)


s_nv = ""
s_m_nv = ""
s_h_nv = "<NV 0>"  # overwritten if NV and  need to be 0 for ATI
if n_NV_cnt>0 or n_argCNT==0 :
	r_dev = os.popen('nvidia-smi -q -d  TEMPERATURE | grep  "GPU Current Temp"').read().splitlines()
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
#		print("max NVidia temp ",s_m_nv)
#		print("NV temps ",s_nv)
		s_h_nv = "<NV " + str(n_nv) + ">"
		gpu_temps = s_nv
hdr_out = hdr_out + s_m_nv 


s_ati=""
s_h_ati="<NA 0>"
s_m_ati = ""
if n_NV_cnt==0 or n_argCNT==0 :
	r_dev = os.popen('sensors | grep "hyst "').read().splitlines()
	n_ati = 0
	m_ati = 0
	for l in r_dev :
		a = l.split("+")
		b=a[1].split(".")
		c=b[0].split("[,]")
		s_ati = s_ati + "<GT" + str(n_ati) + " " + c[0] + ">"
		if float(c[0]) > m_ati :
			m_ati = float(c[0])
		n_ati = n_ati + 1
	if n_ati > 0 :
		s_m_ati = "<TG " + "{:4.1f}".format(m_ati) + ">"
		s_h_ati = "<NA " + str(n_ati) + ">"
		gpu_temps = s_ati
hdr_out = hdr_out + s_m_ati + s_h_nv + s_h_ati

strOUT= strPrefix + hdr_out + strPCT + s_cpu + gpu_temps + strENDING

try :
	data = conn.recv(1024).decode()
#	print("from boinctasks: " + str(data) + " of length " + str(len(data)))
	if not data :
		exit(0)
	conn.send(strOUT.encode())
#	print("sent: ",strOUT)
	conn.close
except BaseException as e:
# the e needs to be logged as str(e) to log file once I figour out how to do that
# but I dont seem to get any errors unless I hit ctrl-c a lot
	exit()
