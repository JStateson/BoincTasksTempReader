Scripts in this folder intall a python script that routes
temperatures to boinctasks.

You must edit the install script and put in your username.
This has been tested under Ubuntu 18.04 and the 
utilities programs "sensors" from lm-sensors needs to be
installed.  if you have nvidia cards, then nvidia-smi also.

The folder /home/YOUR-USERNAME/bin will be created unless it
already exists and two scripts will be copied into it.
A service will be created: /lib/systemd/system/boinctasks_temps

The service can be started or stopped with 
sudo systemctl start boinctasks_temps
suso systemctl stop boinctasks_temps

and should start automatically on any reboot assuming
you did the initial "start"

be sure to mark all the scripts as executable with
chmod +x *.sh
chmod +x *.py

