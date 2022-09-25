#!/bin/bash

echo "Checking to see if the all required programs and packages are installed"

if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv != "Python 3"* ]]
    then
        echo "You've got the wrong version of python, please install Python 3" >&2
    fi 
else
    echo "Error: It looks like you don't have python 3 installed.
    Please head to https://www.python.org/downloads/ and install Python 3" >&2
fi

python3 -m pip install clearing
python3 -m pip install readchar
python3 -m pip install simple-term-menu

python3 main.py