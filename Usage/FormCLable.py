#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import socket
import os
import random
import string
import signal
import sys


tp_dev = os.popen('clinfo | grep -i "Topology"').read().splitlines()
n_item=0
n_nv=0
n_ati=0
n_intel=0
nv_out=""
ati_out=""
intel_out=""


for l in tp_dev :
	a=l.split()
#	print(a[2])
#	print(a[4])
	if "NV" in a[2] :
		nv_out+= a[4] + " "
		n_nv+= 1
	if "ATI" in a[2] :
		ati_out+= a[4] + " "
		n_ati+= 1
	if "INTEL" in a[2] :
		ati_intel+= a[4] + " "
		n_intel+= 1
#print("nv:", n_nv, " ati:",n_ati," n_intel:" , n_intel)
#print(nv_out)


name_dev = os.popen('clinfo | grep  "Device Name"').read().replace("GeForce","").splitlines()
for l in name_dev :
	a=l.split()
	aDevice=a[2]
	if "GTX" in aDevice :
		aDevice+= "-" + a[3]
#	print(aDevice)
	if "Intel" in aDevice :
		continue

# below is nvidia only
nv_dev = os.popen('nvidia-smi -q -d PIDS | grep "GPU 0"').read().replace("GPU 00000000:","").splitlines()
for l in nv_dev :
	a=l.split()
#	print(a[0])
