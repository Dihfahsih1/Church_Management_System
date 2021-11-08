# Church Management System
This is a UCC Bwaise Church management system in which the admin, accountant, department head log into and execute their roles and then submit daily, monthly or annual reports. The records are all achieved and can be retrieved at any point in time.

First Download this project or clone from this repo to your machine

Create virtual environment using `python -m venv venvname` on linux 

Activate the venvname using `source venvname/bin/activate`

Install requirements using `pip install requirements.txt`

Run this on Django shell to exclude contentype data

`python3 manage.py shell`
>>> `from django.contrib.contenttypes.models import ContentType`
>>> `ContentType.objects.all().delete()`
>>> `quit()`

Load workable data into the database using `python manage.py loaddata db.json`
