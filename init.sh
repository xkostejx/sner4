#prepare structure for new module
#python manage.py startapp netmap 
#python manage.py createsuperuser
pip install -r misc/requirements.txt

sudo -u postgres psql -c "DROP DATABASE shodan;"
sudo -u postgres psql -c "DROP DATABASE test_shodan;"
sudo -u postgres psql -c "CREATE DATABASE shodan;"
sudo -u postgres psql -c "ALTER USER root CREATEDB;"

#we did changes on model
python manage.py makemigrations net
python manage.py makemigrations job

#preview sql changes on specific migration
#python manage.py sqlmigrate netmap 0001 

python manage.py migrate

python misc/gen.py > misc/dump.txt
sudo -u postgres psql shodan < misc/dump.txt

python manage.py test --verbosity 2
