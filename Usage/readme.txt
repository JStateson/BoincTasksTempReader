The folder is used to develop and test the scripts used to obtain bus id, power and usage for GPUs

Requred programs lm_sensors, nvidia-smi and clinfo



MakeTable.py : create the file "cc_include.xml" at /etc/boinc-client
-------------

sample output:

<devmap>
<Num_GPUs>9</Num_GPUS>
<1>0 -1 01:00.0 NV GTX-1060-6GB</1>
<2>1 -1 02:00.0 NV GTX-1060-3GB</2>
<3>2 -1 03:00.0 NV GTX-1060-3GB</3>
<4>3 -1 04:00.0 NV P106-100</4>
<5>4 -1 05:00.0 NV GTX-1070</5>
<6>5 -1 08:00.0 NV P106-090</6>
<7>6 -1 0A:00.0 NV GTX-1060-3GB</7>
<8>7 -1 0B:00.0 NV GTX-1060-3GB</8>
<9>8 -1 0E:00.0 NV GTX-1060-3GB</9>
</devmap>

The data is in ascending order 0..n-1 of the output of nvidia-smi or sensors.  Note that this
numnber is not the same as the device 0..n-1 that is shown by the boinc manager or by BoincTasks
The value of -1 is a placeholder for the actual boinc id.  That value is furnished by MSboinc to
update the table (MSBoinc version only)



ShowUsage.py :  Displays usage or power on boinctasks instead of temperature
------------

To test the program, be sure that BoincTasks is running and monitoring your system then execute

./ShowUsage.py <number nvidia board>  <number ati boards) [1]

If a 3rd argument is supplied then usage or power is displayed
If no arguement then temperature is displayed
The above program is renamed to FetchTemps.py and copied into the SystemdService folder
after debugging stuff is removed (if any)
