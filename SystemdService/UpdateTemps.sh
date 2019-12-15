#!/bin/bash
nAnyNVidia=0
bHaveMin=0
if [ ! -e '/bin/nvidia-smi' ] ; then
	nAnyNVidia=`nvidia-smi -L | grep -c GPU`
fi

if [ ! -e '/bin/sensors' ] ; then
	nAnyNVidia=`nvidia-smi -L | grep -c GPU`
	HaveMin=1
	nAnyATI=`sensors | grep -c amd`
fi

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
		echo "failure in FetchTemps" > ./Fetch.Temps.err
	fi
done
