#!/bin/bash
FOLDER="2019/$1/"
mkdir $FOLDER
echo $FOLDER
cp python-template/main.py $FOLDER
cp python-template/Pipfile* $FOLDER
cp -r python-template/input $FOLDER
