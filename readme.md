# Prject 8: Pur Beurre

PurBeurre is a website application running on Django. The objective of the app is to purpose a database of products (linked with the OpenFoodFacts database) and to help users in finding a healthy substitute of a product.

## Prerequisites

- Python 3.6
- Django 2.1+ (2.1.7 used for developpement)
- PostGreSQL database with access to parameter in settings.py in the pur_beurre folder
- All the other required modules are in the requirements.txt file to install before launching the app.


## How to install

First clone or download the project.
(VirtualEnv is recommended to install the requirements)
```bash
$ cd "project/folder"
$ pip install -r requirements.txt
```

## Environment variables

The app is already ready for deployment. But if you need to modify things you will need to do this in the settings.py file

- First enable debug
```python
DEBUG = True
```
- Second enable local database
 ```python
#Production Database
#DATABASES = {'default': dj_database_url.config()}

#Development database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'pur_beurre',
		'USER': 'django',
		'PASSWORD': 'django',
		'HOST': 'localhost',
		'PORT': '',
	}
}
```

- Finally set local file dir
```python
STATIC_URL =  '/static/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE =  'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "staticfiles"),
)

```

## Deployment

It is possible to deploy to Heroku or to your own server.


## Details
You will need to create one superuser to fill the database.
The command for fill the database is in the admin panel.
