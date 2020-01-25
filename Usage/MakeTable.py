#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import socket
import os
import random
import string
import signal
import sys
import os.path
from os import path


bNVidia = path.exists("/usr/bin/nvidia-smi")
nAMD = os.popen("sensors | grep -c amd").read().rstrip('\n')
bAMD = (nAMD != "0")

if bNVidia :
	n=r_dev = os.popen('nvidia-smi --version | grep -c "has failed because"').read().rstrip("\n")
	bNVidia=(n=="0")





n_item=0
ati_out=[]
nv_out=[]
intel_out=[]
out_xml=""
nGPUx=1	# ordinal number of gpus in system

cl_device=[]
board_names_nv=[]
board_pci_nv=[]
board_names_ati=[]
board_pci_ati=[]
board_names_intel=[]
board_pci_intel=[]

coproc_nv=[]
coproc_amd=[]

def lookup_nv(busid ):
	n=len(coproc_nv)
	for i in range(n) :
		if busid == coproc_nv[i] :
			return(i)
	print("software error 1")
	exit(O)


def first_amd(aline ):
	a=aline.split()
	try :
		inx = a.index("AMD")
	except ValueError:
		inx = a.index("(AMD)")
	return(inx+1)


def toHex(s):
	a = int(s)
	b = str(hex(a))
	c = b.replace("0x","")
	if a <= 15 :
		 c="0"+c+":00.0"
	return(c.upper())

if bNVidia : 
	name_dev = os.popen('nvidia-smi -L').read().replace("GeForce","").splitlines()
	for l in name_dev :
		a=l.split()
		aDevice=a[2]
		if "GTX" in aDevice or "RTX" in aDevice :
			aDevice+= "-" + a[3]
#	print(len(a),":",aDevice)
		if len(a) == 7 :
			aDevice+= "-" + a[4]
		board_names_nv.append(aDevice)
#	print(board_names_nv)
#'GTX-1060-6GB', 'GTX-1060-3GB', 'GTX-1060-3GB', 'P106-100', 'GTX-1070', 'P106-090', 'GTX-1060-3GB', 'GTX-1060-3GB', 'GTX-1060-3GB']
	nv_dev = os.popen('nvidia-smi -q -d PIDS | grep "GPU 0"').read().replace("GPU 00000000:","").splitlines()
	for l in nv_dev :
		a=l.split()
		board_pci_nv.append(a[0])
#	print(nv_bus)
# ['01:00.0', '02:00.0', '03:00.0', '04:00.0', '05:00.0', '08:00.0', '0A:00.0', '0B:00.0', '0E:00.0']

	r_dev = os.popen('grep "<bus_id>" "/var/lib/boinc/coproc_info.xml"').read().replace("<",">").splitlines()
	for l in r_dev :
		a=l.split('>')
		h=toHex(a[2])
		coproc_nv.append(h)
#	print(coproc_nv)


	n=len(board_names_nv)
	if n != len(board_pci_nv) :
		print("number of NV boards ",n," does not match the number of bus ids ",len(board_pci_nv))
		exit(1)
	else :
		for i in range(n) :
			out_xml+= "<" + str(nGPUx) + ">"
			j = lookup_nv(board_pci_nv[i])
			out_xml+= str(i) + " " + str(j) + " " + board_pci_nv[i] + " NV " + board_names_nv[i]
			out_xml+= "</" + str(nGPUx) + ">"
			out_xml += "\n"
			nGPUx+= 1

if bAMD :
	name_dev = os.popen('clinfo | grep -i "Board Name"').read().replace("Series","").splitlines()
	inx=first_amd(name_dev[0])
	for l in name_dev :
		a = l.split()
		aDevice=a[inx]
		n = len(a)-inx
		for i in range(n-1):
			 aDevice+= "-" + a[inx+i+1]
		board_names_ati.append(aDevice)
#print(board_names_ati)
# Device Topology (AMD)                           PCI-E, 01:00.0
	nAMD = os.popen('clinfo | grep -i "Device Topology (AMD)"').read().splitlines()
	for l in nAMD :
		a = l.split()
		n=len(a)-1
		aDevice=a[n]
		board_pci_ati.append(aDevice)
#	print(board_pci_ati)
	n = len(board_names_ati)
	if n != len(board_pci_ati) :
		print("number of ati boards ",n," does not match the number of bus ids ",len(board_pci_ati))
		exit(1)
	else :
		for i in range(n) :
			out_xml+= "<" + str(nGPUx) + ">"
			out_xml+= str(i) + " -1 " + board_pci_ati[i] + " ATI " + board_names_ati[i]
			out_xml+= "</" + str(nGPUx) + ">"
			out_xml+= "\n"
			nGPUx+= 1

cc_include="<devmap>\n<Num_GPUs>" + str(nGPUx-1) + "</Num_GPUs>\n"  + out_xml + "</devmap>\n"

if os.geteuid() != 0:
	print(cc_include)
	exit("You need to have root privileges to write to /etc/boinc-client.\nPlease try again, this time using 'sudo'. Exiting.")
file = open("/etc/boinc-client/cc_include.xml","w");
file.write(cc_include)
file.close()

