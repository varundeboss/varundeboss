base_dir=$(dirname "$0")
app_name=$1
python3 $base_dir/manage.py startapp $1
mkdir -p $1/templates
mkdir -p $1/static/css
mkdir -p $1/static/imgs
mkdir -p $1/static/js
touch $1/requirements.txt
touch $1/urls.py