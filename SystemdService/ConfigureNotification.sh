#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# edit this file to put in your email and phone info and then execute it as root
#  sudo ./ConfigurationNotification.sh

# this script configures email using the sendemail program
# http://caspian.dotconf.net/menu/Software/SendEmail/
# if you do no have an email program then install it  with
# sudo apt-get install sendemail
# note this is different than sendmail so be sure to use the E

# if you already have an email progrram then use that one and
# edit the file GiveNotification.sh to send the warning messages


# we will be sending secure mail using AT&T (yahoo) port 587
# a password is required as port 25 is not used
# for AT&T the email is the login name and yahoo is only the domain


# to send a text message find your carrier and use SMS

#U.S. Carrier	SMS Gateway			MMS Gateway
#Altel		@sms.alltelwireless.com		@mms.alltelwireless.com
#AT&T		@txt.att.net			@mms.att.net
#Boost Mobile	@sms.myboostmobile.com		@myboostmobile.com
#Sprint		@messaging.sprintpcs.com	@pm.sprint.com
#T-Mobile	@tmomail.net			@tmomail.net
#U.S. Cellular	@email.uscc.net			@mms.uscc.net
#Verizon	@vtext.com			@vzwpix.com
#Virgin Mobile	@vmobl.com			@vmpix.com

# if not sending a text message then just put your email in the TEXT_ADDRESS field

LOGIN_NAME="----------@att.net"
LOGIN_PASSWORD="------"
SERVER="smtp.att.yahoo.com:587"
TEXT_ADDRESS="--------@txt.att.net"


############# edit only the above 4 lines ################

echo "\
sendemail \
-f "$LOGIN_NAME"   \
-u "System \'\$1\' error: \'\$2\'"  \
-t '"$TEXT_ADDRESS"' \
-s "$SERVER"  \
-o tls=auto \
-xu "$LOGIN_NAME" \
-xp '"$LOGIN_PASSWORD"' \
-m '"\$2"'
" > ./RunSendEmail.sh
chmod +x RunSendEmail.sh
