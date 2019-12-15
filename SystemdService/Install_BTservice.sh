#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi


USERNAME=jstateson
WorkingDirectory="/home/$USERNAME/bin"

if [ ! -e "/lib/systemd/system/boinctasks_temps.service" ] ; then
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
ExecStop="$WorkingDirectory"/UpdateTemps.sh 1" >> /lib/systemd/system/boinctasks_temps.service
fi

if [ ! -d "$WorkingDirectory" ] ; then
	mkdir "$WorkingDirectory"
fi

cp FetchTemps.py "$WorkingDirectory"
cp UpdateTemps.sh "$WorkingDirectory"

# cannot leave the bin directory or its files as root
chown -R "$USERNAME:$USERNAME" "$WorkingDirectory"

