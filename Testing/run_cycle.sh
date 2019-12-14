#!/bin/bash
echo Press CTRL-C to exit
nAnyNVidia=0
if [ ! -e '/bin/nvidia-smi' ] ; then
	nAnyNVidia=`nvidia-smi -L | grep -c GPU`
fi
#  if any nvidia boards, the FetchTemps script will assume no ATI boards
# and vice versa until I figure out how to put both in

while [ : ]
do
	./FetchTemps.py "$nAnyNVidia"
	sleep 10
done
