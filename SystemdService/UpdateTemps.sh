#!/bin/bash
nAnyNVidia=0
HaveMin=0
HaveProblem=0

if [ $1 ] ; then
 rm -f ./lockfile
 exit 0
fi

if [ ! -f '/bin/nvidia-smi' ] ; then
	HaveProblem=`nvidia-smi | grep -c "Reboot the system"`
	if  [ $HaveProblem -eq 0 ] ; then
		nAnyNVidia=`nvidia-smi -L | grep -c GPU`
	else
		rm -f ./lockfile
		/usr/bin/boinccmd --set_gpu_mode never
		ProblemSystem=`uname -n`
		./GiveNotification.sh "$ProblemSystem" "NVidia requested a reboot"
		exit 0
	fi
fi

if [ ! -f '/bin/sensors' ] ; then
	nAnyNVidia=`nvidia-smi -L | grep -c GPU`
	HaveMin=1
	nAnyATI=`sensors | grep -c amd`
fi

# could iterate thru cnt of board and use nvidiia-smi -q -i $f  to see which board is bad
#
echo $nAnyNVidia > ./NumberNvidia
echo $nAnyATI > ./NumberATI


if [ $nAnyATI -gt 0 ] && [  $nAnyNVidia -gt 0 ] ; then
  if [ $nAnyATI -gt $nNVidia ] ; then
   nAnyNVidia = 0
  else
   nAnyATI = 0
  fi
fi


if [ HaveMin ] ; then
 echo 1 > ./lockfile
fi

while [ -e './lockfile' ]
do
	rtncod=`./FetchTemps.py "$nAnyNVidia" "$nAnyATI"`
	if [ $? -ne 0 ] ; then
		rm ./lockfile
		echo "failure in FetchTemps $?" > ./fetchtemps.err
	fi
done
