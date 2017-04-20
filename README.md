Bibliomart Repo
======


This repository is for Bibliomart

----------


Initialisation
-------------

 1. Create a new folder 'bibliomart-src'.
 2. Open termial and traverse to 'bibliomart-src' folder.
 3. Create a new folder inside 'bibliomart-src' as 'bibliomart'.
 4. Create a Virtual Environment :
        `virtualenv -p python3.5 --no-site-packages bibliomart-env`
 5. Activate the environment :
        `source bibliomart-env/bin/activate`
 6. Traverse to bibliomart folder :
        `cd bibliomart`
 7. Clone this repository there :
        `git clone https://github.com/kittycancode/bibliomart.git`
 8. Install required packages :
        `pip install -r requirements.txt`
 9. Initialise Database :
        `python createdb.py`
 4. Start the server :
        `python manage.py runserver`
 5. Go to `http://localhost:8000`
