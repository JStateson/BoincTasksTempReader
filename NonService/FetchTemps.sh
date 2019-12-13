#!/bin/bash
# if an argument is supplied it should be a number and that number indicates how many times
# the temps will be read before qutting.  Use for testing
CYCLE_COUNT=$1
if [[ $CYCLE_COUNT  -gt 0 ]]; then
USE_CYCLE=1
else
USE_CYCLE=0
fi

SLEEP_SECS=6
# count video devices right away
#rm temp.tmp
N_NV=0
if [ -f "/usr/bin/nvidia-smi" ]; then
N_NV=`nvidia-smi -q -d  TEMPERATURE | grep -c  "GPU Current Temp"`
fi

N_ATI=`sensors | grep -c  "hyst "`

while [ 1 ]
do

# sammple output line for parsing CPU temperatures
#Core 0:        +34.0°C  (high = +84.0°C, crit = +100.0°C)
#Core 1:        +35.0°C  (high = +84.0°C, crit = +100.0°C)
#Core 2:        +34.0°C  (high = +84.0°C, crit = +100.0°C)
#Core 3:        +35.0°C  (high = +84.0°C, crit = +100.0°C)

N_CPU=0
M_CPU=0
TEMP_STR=""
sensors | grep "Core" > temp.tmp
input=./temp.tmp
while IFS= read -r line
do
((N_CPU=N_CPU+1))
#echo "$line"
IFS=' ' read -r -a array <<< "$line"
T="${array[2]}"
U="${T:1:-2}"
TEMP_STR="$TEMP_STR $U "
# not going to find the highest, let boinctasks do that
#V="${U/./}"
#if [ $V -gt $M_CPU ] ; then
#((M_CPU=V))
#fi
done < "$input"
CPU_STR="CPU $N_CPU $TEMP_STR"

echo "Number of ATI coprocs" $N_ATI
echo "Number of NVidia coprocs" $N_NV
echo "Number of CPUs: ${N_CPU}"


# sample output line from sensors as parsed for ATI
#temp1:        +29.0°C  (crit = +94.0°C, hyst = -273.1°C)

if [[ $N_ATI -gt 0 ]] ; then
  ATI_STR="ATI ${N_ATI} "
  sensors | grep "hyst " > temp.tmp
  N_ATI=0
  M_ATI=0
  input=./temp.tmp
  while IFS= read -r line
  do
  ((N_ATI=N_ATI+1))
#  echo "$line"
  IFS=' ' read -r -a array <<< "$line"
  T="${array[1]}"
  U="${T:1:-2}"
  V="${U/./}"
  ATI_STR="$ATI_STR $V"
  done < "$input"
#  echo "ATI-OUT: ${ATI_STR}"
else
 ATI_STR="ATI 0"
fi

# sample output line from 7 device NVidia system for parsing study
#        GPU Current Temp            : 53 C
#        GPU Current Temp            : 50 C
#        GPU Current Temp            : 79 C
#        GPU Current Temp            : 57 C
#        GPU Current Temp            : 50 C
#        GPU Current Temp            : 57 C

if [[ $N_NV > 0 ]] ; then
  nvidia-smi -q -d  TEMPERATURE | grep  "GPU Current Temp" > temp.tmp
  M_NV=0
  NV_STR="NV ${N_NV} "
  I_NV=0
  input=./temp.tmp
  while IFS= read -r line
  do
#  echo "$line"
  IFS=' ' read -r -a array <<< "$line"
  T="${array[4]}"
  # multiply by 10 to be consistent
  # U="${T}0 " 
  NV_STR="$NV_STR $T"   # not using time 10 anymore
  ((I_NV=I_NV+1))
  if [ $I_NV -eq $N_NV ]; then
    break
  fi  
  done < "$input"
#  echo "NV-OUT: ${NV_STR}"
else
 NV_STR="NV 0"
fi

python3 InformBoincTasks.py $CPU_STR $ATI_STR $NV_STR
if [ $USE_CYCLE ]; then
 ((CYCLE_COUNT=CYCLE_COUNT-1))
  if [ $CYCLE_COUNT -eq 0 ]; then
  break
 fi
fi
sleep $SLEEP_SECS
done

