# Check the python version first

PS C:\VSCode> python -V
Python 3.10.4

# Create a new folder "Dev" for example 

PS C:\VSCode\Dev> dir
PS C:\VSCode\Dev> 

# Check if you have by running "pip show virtualenv" installed

PS C:\VSCode\Dev> pip show virtualenv
Name: virtualenv
Version: 20.14.1
Summary: Virtual Python Environment builder
Home-page: https://virtualenv.pypa.io/
Author: Bernat Gabor
Author-email: gaborjbernat@gmail.com
License: MIT
Location: c:\users\administrator\appdata\local\programs\python\python310\lib\site-packages
Requires: distlib, filelock, platformdirs, six
Required-by:

# if NOT install, please install using command "pip install virtualenv"

PS C:\VSCode\Dev> pip install virtualenv 
Collecting virtualenv
  Downloading virtualenv-20.14.1-py2.py3-none-any.whl (8.8 MB)

# Let me show you two ways to create virtual environment now. I'll create 

1- "myEnv1" and 
2- "myEnv2"

# Switch to a "cmd" terminal now instead of default PS as it will show the virtual evn you will be working in

===============
## Method 1
===============

# Create a folder where you will create your virtual env (your project). For example "myEnv1" here now

C:\VSCode\Dev>mkdir myEnv1  

C:\VSCode\Dev>dir
 Volume in drive C has no label.
 Volume Serial Number is 0E5C-FB3E

 Directory of C:\VSCode\Dev

04/18/2022  01:37 PM    <DIR>          .
04/18/2022  01:37 PM    <DIR>          ..
04/18/2022  01:37 PM    <DIR>          myEnv1      
               0 File(s)              0 bytes      
               3 Dir(s)  326,395,809,792 bytes free

# cd into that folder 

C:\VSCode\Dev>cd myEnv1
C:\VSCode\Dev\myEnv1>

# Create virtual environment now inside this folder
C:\VSCode\Dev\myEnv1>virtualenv .
created virtual environment CPython3.10.4.final.0-64 in 3471ms
  creator CPython3Windows(dest=C:\VSCode\Dev\myEnv1, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

C:\VSCode\Dev\myEnv1>

===============
## Method 2
===============

# another way is to go up to parent folder (Dev here...) and then run the name of folder (myEnv2 here...) you want to create virtual ennvironment in. 
# for example 

virtualenv myEnv2

# Now you will see two folder representing two virutalenv

C:\VSCode\Dev>virtualenv myEnv2
created virtual environment CPython3.10.4.final.0-64 in 629ms
  creator CPython3Windows(dest=C:\VSCode\Dev\myEnv2, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

C:\VSCode\Dev>dir
 Volume in drive C has no label.
 Volume Serial Number is 0E5C-FB3E

 Directory of C:\VSCode\Dev

04/18/2022  01:40 PM    <DIR>          .
04/18/2022  01:40 PM    <DIR>          ..
04/18/2022  01:39 PM    <DIR>          myEnv1      
04/18/2022  01:40 PM    <DIR>          myEnv2      
               0 File(s)              0 bytes      
               4 Dir(s)  326,370,992,128 bytes free

# Check now

 Directory of C:\VSCode\Dev\myEnv1

04/18/2022  01:39 PM    <DIR>          .
04/18/2022  01:39 PM    <DIR>          ..
04/18/2022  01:39 PM                42 .gitignore
04/18/2022  01:39 PM    <DIR>          Lib
04/18/2022  01:39 PM               442 pyvenv.cfg
04/18/2022  01:39 PM    <DIR>          Scripts
               2 File(s)            484 bytes
               4 Dir(s)  326,369,558,528 bytes free

 Directory of C:\VSCode\Dev\myEnv2

04/18/2022  01:40 PM    <DIR>          .
04/18/2022  01:40 PM    <DIR>          ..        
04/18/2022  01:40 PM                42 .gitignore
04/18/2022  01:40 PM    <DIR>          Lib
04/18/2022  01:40 PM               442 pyvenv.cfg
04/18/2022  01:40 PM    <DIR>          Scripts
               2 File(s)            484 bytes
               4 Dir(s)  326,372,810,752 bytes free

# Again make sure you are using "cmd" terminal now and let's activate one of those environments

C:\VSCode\Dev>myEnv1\Scripts\activate.bat

(myEnv1) C:\VSCode\Dev>pip list
Package    Version
---------- -------
pip        22.0.4 
setuptools 62.1.0 
wheel      0.37.1 

(myEnv1) C:\VSCode\Dev>pip freeze

# Deactivate virtual environment to exit from virtual enviornment like below
(myEnv1) C:\VSCode\Dev>deactivate

# Now check into another one too 

C:\VSCode\Dev>myEnv2\Scripts\activate.bat 

(myEnv2) C:\VSCode\Dev>pip list   
Package    Version
---------- -------
pip        22.0.4 
setuptools 62.1.0 
wheel      0.37.1 

(myEnv2) C:\VSCode\Dev>pip freeze

(myEnv2) C:\VSCode\Dev>

# Let's try to install something different in them

# Install DJango in myEnv1

# Activate myEnv1
C:\VSCode\Dev>myEnv1\Scripts\activate.bat

# install django's version "2.0.7" by running "pip install django==2.0.7"

C:\VSCode\Dev>myEnv1\Scripts\activate.bat

(myEnv1) C:\VSCode\Dev>pip install django==2.0.7
Collecting django==2.0.7
  Downloading Django-2.0.7-py3-none-any.whl (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 6.3 MB/s eta 0:00:00
Collecting pytz
  Downloading pytz-2022.1-py2.py3-none-any.whl (503 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 503.5/503.5 KB 6.2 MB/s eta 0:00:00
Installing collected packages: pytz, django
Successfully installed django-2.0.7 pytz-2022.1

(myEnv1) C:\VSCode\Dev>

# install django's latest version by running "pip install django"

(myEnv2) C:\VSCode\Dev\myEnv2>pip install django
Collecting django
  Downloading Django-4.0.4-py3-none-any.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 5.0 MB/s eta 0:00:00
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Collecting asgiref<4,>=3.4.1
  Using cached asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0.4 sqlparse-0.4.2 tzdata-2022.1

(myEnv2) C:\VSCode\Dev\myEnv2>

# Now if you run pip freeze, you will see that both environments are separate now for your develpment work

### Note: pip list lists everything, and pip freeze installs everything installed by pip

# ======== myEnv1 ========
(myEnv1) C:\VSCode\Dev\myEnv1>pip freeze
Django==2.0.7
pytz==2022.1

(myEnv1) C:\VSCode\Dev\myEnv1>pip list
Package    Version
---------- -------
Django     2.0.7  
pip        22.0.4 
pytz       2022.1 
setuptools 62.1.0 
wheel      0.37.1 

# ======== myEnv2 ========
(myEnv2) C:\VSCode\Dev\myEnv2>pip freeze
asgiref==3.5.0
Django==4.0.4  
sqlparse==0.4.2
tzdata==2022.1 

(myEnv2) C:\VSCode\Dev\myEnv2>pip list   
Package    Version
---------- -------
asgiref    3.5.0  
Django     4.0.4  
pip        22.0.4 
setuptools 62.1.0 
sqlparse   0.4.2  
tzdata     2022.1 
wheel      0.37.1 

