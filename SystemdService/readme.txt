The Scripts in this folder intall bash and python script that
route temperatures to boinctasks.

You must edit the install script and put in your username.
This has been tested under Ubuntu 18.04 and the 
utilities programs "sensors" from lm-sensors needs to be
installed.  if you have nvidia cards, then nvidia-smi also.

The folder /home/YOUR-USERNAME/bt_bin will be created unless it
already exists and all scripts will be copied into it.
A service will be created: /lib/systemd/system/boinctasks_temps
and a pair small scripts to start and stop the service.
DO not download the files from GitHub into the bt_bin folder,
use another folder.

The service can be started or stopped with 
sudo systemctl start boinctasks_temps
sudo systemctl stop boinctasks_temps
The scripts "tstart.sh" asnd "tstop.sh" can be used also


The service will start automatically on any reboot assuming
you did the initial "start"

be sure to mark all the scripts as executable after downloading
chmod +x *.sh
chmod +x *.py

The script GiveNotification is used to inform of a serious
problem.  Be sure to edit that script if you wish to change
the method of notification.  Currently, the only problem
recognized is the reboot request form the NVidia driver.
The BT service will attempt to stop all GPU activity when
this happens and will run the GiveNotification script.

Read the configuration file to see how to email a
warning or send a text mesaage.
