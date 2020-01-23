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
To test the motification script run something like
./GiveNotification.sh "test failure"  "this is a test"

January 22, 2020

feature added:  Ability to show wattage for nvidia and ati and
to be able to correlate* the usage to the bus id of the GPU device.

To enable these features, edit the bash script "pdateTemps.sh and
add true or false to indicate which one or both are to be seen.
Also remove the comment to allow the bus id to be written to
the /usr/boinc-client/cc_include.xml file.  When both are shown
the temperatures for the CPU (if any running) are set to 0 to
indicate that wattage is being displayed instead of temperatures.


*bus id correlation requires using the MSboinc program.  Alternately,
you can inspect the file at /etc/boinc-client/cc_include.xml and
compare the order agains the values for usage or power in the
temperature column of BoincTasks.
