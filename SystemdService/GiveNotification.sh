echo  $1:***ERROR*** $2
if [ -f "./RunSendEmail.sh" ] ; then
./RunSendEmail "$1"  "$2"
fi

