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

3. Include the followings to your project's settings.py file::

  	import djcelery
		djcelery.setup_loader()
		BROKER_URL = 'django://'
		CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
		CELERY_RESULT_BACKEND = 'rpc://'
		CELERY_RESULT_PERSISTENT = False
		REST_FRAMEWORK = {
		    'DEFAULT_PERMISSION_CLASSES': [
			'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
		    ]
		}


4. Include the followings to URLconf in your project urls.py like this::

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'', include('AlbumCreator.urls', namespace="AlbumCreator")),
]

5. You can run python manage.py fetchphotos to start fetch manually from shell.

6. You can run celery -A projectname worker -B to start automated fetch in every 20 minutes
