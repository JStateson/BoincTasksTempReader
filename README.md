# Tools send temperature information to BoincTasks for display from Linux systems
Optionally Wattage can be sent or both wattage and temps can be alternatately displayed

This repository contains bash scripts and python code that send temperature info
to BoincTasks.  You need python version 3,  lm-sensors 3.40 and (optional) clinfo.  
```
sudo apt-get install python3;
sudo apt-get install m-sensors;
sudo apt-get install clinfo
```
Sensors 3.40 provide CPU and ATI temperatures and nvidia-smi provides NVidia temps

If you are running a firewall (default in Ubuntu is OFF) then be sure to allow 
port 31417 to get through the firewall

The folder SystemdService has an install script that creats a sevice to run
the program on startup.  You must first run  "sudo systemctl start boinctasks_temps"
Currently, the script does not start on boot so you need to start it manually

The tar file contains the Service install and has the newest code.
Before downloading the tarball run these
```
nvidia-smi
sensors
clinfo
python3 --version
```

On occassion (stuck GPU), the NVidia driver asks for a reboot.  This is tracked and
a GPU stop running is issued to boinc.  A text message or email can be sent if you
run the configure script before running the install script.  The configure script is
set up to use the sendEmail tool, version 1.56

The script chg_intel_freq.sh can be used to lower the frequency of the Intel CPU if it is
overheating. Usually only one step down is needed.  Run the script with no arguments
and if no frequencies are listed then the script wont work.

1-22-2020 feature add:  Wattage can be displayed instead of temperature and
correlated with the bus id of the graphics card.  Edit the script UpdateTemps.sh and
set the values of bShowTemps and/or bShowWatts.  If you have different quality video
boards then the BOINC board IDs will not match the NVidia linux kernel IDs so 
you must uncomment the line in the script UpdateTemps.sh so that MakeTable.py can run
This python script requires the clnfo tool to map the IDs to the correct coprocessor

*QUICK TEST*
Bring up boinctasks and select your linux system so the tasks are visible
If you have 2 NVidia board, no ATI and want to see temps (there is a 10 second delay):
```
./FetchTemps.py 2 0 0
```
To see wattage in place of temps
```
./FetchTemps.py 2 0 1
```
If your NVidia boards are not identical then first run the following to build a translation table
```
sudo ./MakeTable.py
```
For a pair of ATI boards:
```
./FetchTemps.py 0 2 0
```
To start or stop the service
```
sudo ./start_temps.sh
sudo ./halt_temps.sh
```
