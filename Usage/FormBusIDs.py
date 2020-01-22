#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#nvidia-smi -q -d PIDS | grep "GPU 0"
#GPU 00000000:0A:00.0
# was a count of nvidia boards passed to us?


import time
import socket
import os
import random
import string
import signal
import sys

# clinfo | grep "Topology (AMD)"


n_argCNT = len(sys.argv) - 1
n_NV_cnt  = 0
n_ATI_cnt = 0
r_dev = ""

out_str=""

if n_argCNT != 0 :
	n_NV_cnt = int(sys.argv[1])
	n_ATI_cnt = int(sys.argv[2])
if n_NV_cnt>0 :
	r_dev = os.popen('nvidia-smi -q -d PIDS | grep "GPU 0"').read().splitlines()
	n_nv = 0
	out_str = out_str + "<NV_GPU>\n"
	for l in r_dev :
		a = l.split(" ")
		out_str = out_str + "<BUS_ID>" + a[1] + "</BUS_ID>\n"
		n_nv = n_nv + 1
	out_str = out_str + "</NV_GPU>\n"

if n_ATI_cnt>0 :
	r_dev = os.popen('clinfo | grep "Topology (AMD)"').read().splitlines()
	n_at = 0
	out_str = out_str + "<ATI_GPU>\n"
	for l in r_dev :
		a = l.split()
		out_str = out_str + "<BUS_ID>" + a[4] + "</BUS_ID>\n"
		n_at = n_at + 1
	out_str = out_str + "</ATI_GPU\n>"

print(out_str)
#file = open("/etc/boinc-client/cc_include.xml","w");
#file.write(out_str)
#file.close()
