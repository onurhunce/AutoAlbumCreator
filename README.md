# AutoAlbumCreator
Album Creator is a smart Django application to create automated photo albums.
AlbumCreator is a smart Django application to create automated photo albums. The app runs every 20 minutes and fetch the last photos posted on twitter (under the hashtag #carnival ) since the last fetching and creates a photo album. 

Quick start
-----------

1. run pip install -r requirements command in the AlbumCreator directory.


2. Add "AlbumCreator", "djcelery", "kombu.transport.django", "rest_framework" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'AlbumCreator',
    	  'djcelery',
    	  'kombu.transport.django',
    	  'rest_framework',
    ]

3. You can run python manage.py fetchphotos to start fetch manually from shell.

4. You can run celery -A projectname worker -B to start automated fetch in every 20 minutes
