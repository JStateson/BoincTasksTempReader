echo  $1:***ERROR*** $2
if [ -f "./RunSendEmail.sh" ] ; then
./RunSendEmail.sh "$1"  "$2"
fi

