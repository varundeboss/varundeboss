#!/usr/bin/env bash

base_dir=$PWD
echo "PWD: "$base_dir
app_name=$1

cd apis
python3 $base_dir/manage.py startapp $app_name
mkdir -p $app_name/static/templates
mkdir -p $app_name/static/images
mkdir -p $app_name/static/css
mkdir -p $app_name/static/js
touch $app_name/requirements.txt
touch $app_name/urls.py
cd $base_dir