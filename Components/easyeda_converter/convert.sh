#!/bin/bash

if [ -z $1 ] ; then
	echo "Run with the JLC or LTSC part number as the argument"
	echo "ex:"
	echo "./convert.sh C2927029"
	exit 1
fi

echo "Converting $1"
source vnev/bin/activate
easyeda2kicad --full --overwrite --lcsc_id $1
echo "Done!"

