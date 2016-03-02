from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_all_images_from_database, name='all_photos'),
    url(r'^popular/$', views.show_popular_photos, name='popular'),
    url(r'^export/$', views.post_photos_to_facebook, name='popular'),
    url(r'^fetch/$', views.fetch_photos_manually_from_browser, name='fetch'),
]