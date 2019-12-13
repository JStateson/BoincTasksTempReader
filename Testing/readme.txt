This phyton3 script is being tested on Ubuntu 18.04 and uses sensors and nvidia-smi to obtain
temperatures.  ATI is not covered yet.  The values are formatted into a string that is compatible
with BoincTasks.  To test this program, copy it to your home folder.  Bring up Boinctasks on your windows system and make sure the linux system is identified.  On the linux system, run this script

./FetchTemps.py

The program will run once and then exit. The output should look like the following


FetchTemps.py
jstateson@h110btc:~/Projects/BoincTasks/Testing$ ./FetchTemps.py
Connection Established: ('192.168.1.241', 63229)
max cpu temp  39.0
CPU temps  <CT0 40><CT1 39><CT2 39><CT3 38>
max NVidia temp  <TG 62.5>
NV temps  <GT0 61><GT1 55><GT2 56><GT3 82><GT4 57><GT5 64>
from boinctasks: <BT> of length 5
sent:  <TThrottle><HN:h110btc><PV 7.72><AC 0><TC 39.0><TG 62.5><NV 6><NA 0><DC 100><DG 100><CT0 40><CT1 39><CT2 39><CT3 38><GT0 61><GT1 55><GT2 56><GT3 82><GT4 57><GT5 64><RS?G_jWJt><AA1><SC77><SG80><XC100><MC2><TThrottle>
from boinctasks:  of length 0


The Boinctasks "task" display for the above is named "linux_nv_temps.png"
