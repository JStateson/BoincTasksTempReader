#!/bin/bash
nAnyNVidia=0
nAnyATI=0
HaveMin=0
HaveProblem=0


# change the next two lines to show either one or both
bShowTemps=true
bShowWatts=false

bEnableTemps=1
bEnableWatts=2

iWhatToShow=0

if $bShowTemps  ; then
        (( iWhatToShow|=bEnableTemps ))
fi

if $bShowWatts  ; then
	(( iWhatToShow|=bEnableWatts ))
fi


if [ $1 ] ; then
 rm -f ./lockfile
 exit 0
fi

if [ -f '/usr/bin/nvidia-smi' ] ; then
	HaveProblem=`nvidia-smi | grep -c "Reboot the system" | tr -d "\n"`
	if [[ "$HaveProblem"  -eq "0" ]] ; then
		nAnyNVidia=`nvidia-smi -L | grep -c GPU | tr -d "\n"`
	else
		rm -f ./lockfile
		/usr/bin/boinccmd --set_gpu_mode never
		ProblemSystem=`uname -n`
		./GiveNotification.sh "$ProblemSystem" "NVidia requested a reboot"
		exit 0
	fi
fi

if [ ! -f '/usr/bin/sensors' ] ; then
	nAnyNVidia=`nvidia-smi -L | grep -c GPU | tr -d "\n"`
	HaveMin=1
	nAnyATI=`sensors | grep -c amd | tr -d "\n"`
fi

# could iterate thru cnt of board and use nvidiia-smi -q -i $f  to see which board is bad
#
echo -n $nAnyNVidia > ./NumberNvidia
echo -n $nAnyATI > ./NumberATI

# pick the biggest one until I figure out how to report both to boinctasks
if [[ "$nAnyATI" -gt "0" ]] && [[  "$nAnyNVidia" -gt "0" ]] ; then
  if [ $nAnyATI -gt $nNVidia ] ; then
   nAnyNVidia = 0
  else
   nAnyATI = 0
  fi
fi


if [ HaveMin ] ; then
 echo -n 1 > ./lockfile
fi

# uncomment below line to get bus id info
#./MakeTable.py

iLast=0
iShow=0
while [ -e './lockfile' ]
do
	if [ $iWhatToShow -eq 3 ] ; then
		(( iShow=iLast ))
		(( iLast+=1 ))
		if [ $iLast -eq 2 ] ; then
			iLast=0
		fi
	else
		if $bShowTemps ; then
			iShow=0
		fi
		if $bShowWatts ; then
			iShow=1
		fi
	fi

if [ $iShow -eq 1 ] ; then
	showusage="1"
else
	showusage="0"
fi
#echo ./FetchTemps.py "$nAnyNVidia" "$nAnyATI" "$showusage"
	./FetchTemps.py "$nAnyNVidia" "$nAnyATI" "$showusage"
	if [ $? -ne 0 ] ; then
		rm ./lockfile
		echo "failure in FetchTemps $?" > ./fetchtemps.err
	fi
done
