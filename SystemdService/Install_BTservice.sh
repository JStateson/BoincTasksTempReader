#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi


# edit this file and put in your username


# IN ADDITION to putting in  username, if you
# wish to have the program send a message in event of a
# probllem then READ the script ConfigureNotifications.sh
# and IF NECESSARY run that script BEFORE running this one
# That script makes use of the utility sendemail and that
# must be installed.  If you already have an email tool then
# edit the file GiveNotification.sh to work with your exiting
# email using the ConfigureNotifications.sh as a guide

USERNAME=jstateson
WorkingDirectory="/home/$USERNAME/bt_bin"

####### should not need to edit anything below this line #####


echo "\
[Unit]
Description=Send Boinctask Temps
After=network-online.target
[Service]
Type=simple
Nice=10
User="$USERNAME"
WorkingDirectory="$WorkingDirectory"
ExecStart="$WorkingDirectory"/UpdateTemps.sh
ExecStop="$WorkingDirectory"/UpdateTemps.sh 1" > /lib/systemd/system/boinctasks_temps.service

if [ ! -d "$WorkingDirectory" ] ; then
	mkdir "$WorkingDirectory"
fi

chmod +x *.sh
chmod +x *.py

# need to remove root on RunSendEmail.sh which may not exist
chown -R "$USERNAME:$USERNAME" *.sh

cp *.py "$WorkingDirectory"
cp *.sh "$WorkingDirectory"

# cannot leave the bin directory or its files as root
chown -R "$USERNAME:$USERNAME" "$WorkingDirectory"
