## Now, let's check this out

What Python version can I use with Django?¶
Django version	Python versions

Reference: https://docs.djangoproject.com/en/4.0/intro/tutorial01/


## Let's check this https://docs.djangoproject.com/en/4.0/faq/install/#faq-python-version-support

so with python versions 3.8, 3.9, 3.10 I have to use 4.0. Let's remove this and install the lastest one

python -m django --version

pip uninstall django
pip uninstall pytz

# Installing latest version of Django

(myEnv1) C:\VSCode\Dev>pip install django
Collecting django
  Using cached Django-4.0.4-py3-none-any.whl (8.0 MB)
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.4.1
  Using cached asgiref-3.5.0-py3-none-any.whl (22 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0.4 sqlparse-0.4.2 tzdata-2022.1

(myEnv1) C:\VSCode\Dev>pip freeze
asgiref==3.5.0
Django==4.0.4  
sqlparse==0.4.2
tzdata==2022.1 

## Check the version now

(myEnv1) C:\VSCode\Dev>python -m django --version 
4.0.4

## Now let's explore the command "django-admin" and create a new project
django-admin startproject myDjango

## Run the server "python manage.py runserver"

(myEnv1) C:\VSCode\Dev\myDjango>python manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 18, 2022 - 14:54:36
Django version 4.0.4, using settings 'myDjango.settings'
Starting development server at http://127.0.0.1:8000/   
Quit the server with CTRL-BREAK.

## Now to http://127.0.0.1:8000/ and the website should be up and running

## You will also notice the logging when you reload the webpage

[18/Apr/2022 14:55:43] "GET / HTTP/1.1" 200 10697
[18/Apr/2022 14:55:43] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[18/Apr/2022 14:55:43] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
[18/Apr/2022 14:55:43] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 
304 0
[18/Apr/2022 14:55:43] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0

## Make sure there is nothign pending to migrate by running below command

(myEnv1) C:\VSCode\Dev\myDjango>python manage.py migrate  
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

## Creating an admin user "python manage.py createsuperuser"

=====
UserName: Sunil
Password: P@ssw0rd1
=====

(myEnv1) C:\VSCode\Dev\myDjango>python manage.py createsuperuser   
Username (leave blank to use 'administrator'): Sunil
Email address:
Password:
Password (again):
Error: Blank passwords aren't allowed.

Password:
Password (again):
Superuser created successfully.

## access the admin page now 
http://127.0.0.1:8000/admin/

## Let's create an app now

(myEnv1) PS C:\VSCode\Dev\myDjango> python .\manage.py startapp myProducts

## Let's explore
(myEnv1) PS C:\VSCode\Dev\myDjango> cd .\myProducts\
(myEnv1) PS C:\VSCode\Dev\myDjango\myProducts> dir


    Directory: C:\VSCode\Dev\myDjango\myProducts


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         4/19/2022  12:31 PM                migrations
-a----         4/19/2022  12:31 PM             66 admin.py
-a----         4/19/2022  12:31 PM            158 apps.py
-a----         4/19/2022  12:31 PM             60 models.py
-a----         4/19/2022  12:31 PM             63 tests.py
-a----         4/19/2022  12:31 PM             66 views.py
-a----         4/19/2022  12:31 PM              0 __init__.py


## Make moduel myProducts and the Products inside models.py


from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()



## update settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myProducts',
]

## then run


(myEnv1) C:\VSCode\Dev\myDjango>python manage.py makemigrations        
Migrations for 'myProducts':
  myProducts\migrations\0001_initial.py
    - Create model Product

(myEnv1) C:\VSCode\Dev\myDjango>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myProducts, sessions
Running migrations:
  Applying myProducts.0001_initial... OK

