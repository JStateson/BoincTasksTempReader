# BoincTasks
This repository contains bash scripts and python code that send temperature
information to BoincTasks.  You need python version 3 and lm-sensors 3.40

sudo apt install python3; sudo apt install lm-sensors

Sensors 3.40 provides CPU and ATI temperatures and is required

If you are running a firewall (default in Ubuntu is OFF) then be sure to allow 
port 31417 to get through the firewall

The folder SystemdService has an install script that creats a sevice to run
the program on startup.  You must first run  "sudo systemctl start boinctasks_temps"
Currently, the script does not start on boot so you need to start it manually

Before installing the service you should run the scripts in the "NonService" 
folder to verify you have all the required files.  There are readme's in each folder.
Suggest you create a "temp" folder and download the entire "zip" into it.  The install
puts files into the home/username/bt_bin folder.  The testing folder has debugging info
and runs like the NonService but shows temp values

On occassion (stuck GPU), the NVidia driver asks for a reboot.  This is tracked and
a GPU stop running is issued to boinc.  A text message or email can be sent if you
run the configure script before running the install script.

The script chg_intel_freq.sh can be used to lower the frequency of the Intel CPU if it is
overheating. Usually only one step down is needed.  Run the script with no arguments
and if no frequencies are listed then the script probably wont work.
