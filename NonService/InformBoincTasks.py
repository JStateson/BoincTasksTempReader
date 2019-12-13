import sys
import socket
import os
import subprocess

BoincTasksHost="192.168.1.241"
port=31416
hostname=os.uname()[1]

#subprocess.check_call("./script.ksh %s %s %s" % (agr1, str(arg2), arg3),   shell=True)
# read the following for security and other considerations
# https://stackoverflow.com/questions/13745648/running-bash-script-from-within-python


# count the arguments:  CPU  N ... ATT N ... NV N ...
# intel not programmed yet
strOut = ""
arguments = len(sys.argv) - 1
position = 1
while (arguments >= position):
    strOut+= sys.argv[position] + " "
    position = position + 1
print (strOut, " ", hostname)

# sample of TCP message  from 6 core xeon with single nvidia board
# <NV 1> is the one nvidia
# <AT 1> is used for ati
# <CT0  16.5> is the temp for the first cpu
# <PV 7.72> is verison number
# do not know the rest
#<TThrottle><HN:jyslinux1><PV 7.72><AC 1><TC 22><TG 31><NV 1><NA 2><DC 100><DG 100><CT0 16.5><CT1 21.9><CT2 21.9><CT3 21.8><CT4 18.4><CT5 21.2><GT0 31.0><RS?G_jWJt><AA1><SC77><SG80><XC100><MC2><TThrottle>

strPrefix="<PV 7.72><AC 1><TC 22><TG 31>"


# do cpus first
strCPU=""
position=2
ncpu= int(sys.argv[position])
cnt=0
while ncpu > 0 :
	position+= 1
	strCPU+= "<ct" + str(cnt) + " " + sys.argv[position] + ">"
	ncpu-= 1
	cnt+= 1
# do any ATI next
strATI=""
position+= 2
nATI= int(sys.argv[position])
cnt=1
while nATI > 0 :
	position+= 1
	strATI+= "<AT" + str(cnt) + " " + sys.argv[position] + ">"
	nATI-= 1
	cnt+= 1
# do any NVidia
strNV=""
position+= 2
nNV= int(sys.argv[position])
cnt=1
while nNV > 0 :
	position+= 1
	strNV+= "<NV" + str(cnt) + " " + sys.argv[position] + ">"
	nNV-= 1
	cnt+= 1

# might need the following?
strUNK_NV="<NA 2><DC 100><DG 100>"

strENDING="<GT0 31.0><RS?G_jWJt><AA1><SC77><SG80><XC100><MC2><TThrottle>"

strOUT= strPrefix + strATI + strNV + strCPU + strENDING

print(strOUT)
