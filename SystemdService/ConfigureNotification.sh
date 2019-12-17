
# edit this file to put in your email and phone info and then execute it
#   ./ConfigurationNotification.sh

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

LOGIN_NAME="username@att.net"
LOGIN_PASSWORD="password"
SERVER="smtp.att.yahoo.com:587"
TEXT_ADDRESS="phonenumber@txt.att.net"  # eg: 9876543210@txt.att.net put in +1 or whever might be neede


############# edit only the above 4 lines ################


echo -n  "sendEmail " > ./RunSendEmail.sh
echo -n  "-f $LOGIN_NAME " >> ./RunSendEmail.sh
echo -ne "-u \\\'\$1\\\' " >> ./RunSendEmail.sh
echo -n "-t '$TEXT_ADDRESS' " >> ./RunSendEmail.sh
echo -n "-s $SERVER " >> ./RunSendEmail.sh
echo -n "-o tls=auto " >> ./RunSendEmail.sh
echo -n "-xu '$LOGIN_NAME' " >> ./RunSendEmail.sh
echo -n "-xp '$LOGIN_PASSWORD' " >> ./RunSendEmail.sh
echo -e "-m \\\'\$2\\\' " >> ./RunSendEmail.sh
chmod +x RunSendEmail.sh
