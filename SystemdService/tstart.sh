#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

rm -f fetchtemps.err
sudo systemctl start boinctasks_temps

