#!/bin/bash

venv_dir="$HOME/bdossp_sp16"

if [ ! -d $venv_dir ]
then
	virtualenv $venv_dir
fi

source $venv_dir/bin/activate

pip install -r requirements.txt
