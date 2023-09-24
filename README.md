# About Medigital webapp
This is a web application for a fictitious healthcare system Medigital, created in popular Python web framework - Django

# Requirements
To install all the required packages listed in "requirements.txt", make sure you're positioned in a directory in 
which "manage.py" is located. Then, in shell, run:
```
pip install -r requirements.txt
```

# Migrate the database
To migrate the database open terminal in project directory and run:
```
python manage.py makemigrations
python manage.py migrate
```

# Collect static files
```
python manage.py collectstatic
```

# Creating Superuser
To create superuser open terminal and type:
```
python manage.py createsuperuser
```

# Start the app locally
To start the webapp locally use:
```
python manage.py runserver
```
Then go to http://127.0.0.1:8000 in your browser.
