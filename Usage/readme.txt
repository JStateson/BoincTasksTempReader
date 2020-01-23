The folder is used to develop and test the scripts used to obtain bus id, power and usage for GPUs

Requred programs lm_sensors, nvidia-smi and clinfo



FormBusIDs.py : create the file "cc_include.xml" at /etc/boinc-client
-------------

sample output:

NV_GPU>
<BUS_ID>00000000:01:00.0</BUS_ID>
<BUS_ID>00000000:02:00.0</BUS_ID>
<BUS_ID>00000000:03:00.0</BUS_ID>
<BUS_ID>00000000:04:00.0</BUS_ID>
<BUS_ID>00000000:05:00.0</BUS_ID>
<BUS_ID>00000000:08:00.0</BUS_ID>
<BUS_ID>00000000:0A:00.0</BUS_ID>
<BUS_ID>00000000:0B:00.0</BUS_ID>
<BUS_ID>00000000:0E:00.0</BUS_ID>
</NV_GPU>

The data is in ascending order 0..n-1 of the output of nvidia-smi or sensors.  Note that this
numnber is not the same as the device 0..n-1 that is shown by the boinc manager or by BoincTasks




ShowUsage.py :  Displays usage or power on boinctasks instead of temperature
------------

To test the program, be sure that BoincTasks is running and monitoring your system then execute

./ShowUsage.py <number nvidia board>  <number ati boards) [1]

If a 3rd argument is supplied then usage or power is displayed
If no arguement then temperature is displayed
