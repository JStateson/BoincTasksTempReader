# BoincTasks
This repository contains bash scripts and python code that sends temperature
information to BoincTasks.

The folder SystemdService has an install script that creats a sevice to run
the program on startup.  However, you must first run
 "sudo systemctl start boinctasks_temps"

Before it will start up on boot.


Before installing the service you should run the scripts in the "NonService" 
folder to verify you have all the required files.

There are readme's in each folder.

Suggest you create a "temp" folder and download the entire "zip" into it.

