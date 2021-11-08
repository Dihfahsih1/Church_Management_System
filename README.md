# Church_Management_System
This is a UCC Bwaise Church management system in which the admin, accountant, department head log into and execute their roles and then submit daily, monthly or annual reports. The records are all achieved and can be retrieved at any point in time.

First Download this project or clone from this repo to your machine

Create virtual environment using `python -m venv venvname` on linux 

Activate the venvname using `source venvname/bin/activate`

Install requirements using `pip install -r requirements.txt`

Configure the database credetials in `settings.py`

Run migrations to create the tables in the database `python manage.py migrate`

Load workable data into the database using `python manage.py loaddata project_dump.json`
