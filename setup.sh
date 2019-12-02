#!/bin/bash
if [ "$#" -eq 2 ]; then
	FOLDER="$1/$2"
elif [ "$#" -eq 1 ]; then
	FOLDER="2019/$1"
else 
	echo "Wrong number of arguments!"
	exit 1
fi
mkdir $FOLDER
echo $FOLDER
cp python-template/main.py $FOLDER
cp python-template/Pipfile* $FOLDER
cp -r python-template/input $FOLDER
