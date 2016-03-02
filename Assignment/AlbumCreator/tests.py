from django.test import TestCase, LiveServerTestCase
from AlbumCreator.models import Photo, Album


class TestAlbumCreator(TestCase, LiveServerTestCase):

    """
    Testing all url links which address views and get requests. Testing
    passing variables.
    """
    def test_main_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('images' in response.context)


    def test_popular_photos_page(self):
        response = self.client.get('/popular/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('popular_photos' in response.context)


    def test_api_page(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 200)


    def test_api_data_page(self):
        response = self.client.get('/apiphotos/')
        self.assertEqual(response.status_code, 200)


    def test_dump_page(self):
        response = self.client.get('/wrong/input')
        self.assertEqual(response.status_code, 404)

    """
    Testing Models.
    """
    def test_creating_new_photo_object(self):
        new_album = Album.objects.create(name="testalbum", album_capacity=100)
        new_photo = Photo.objects.create(url_name="asda.jpg",
                                         album=new_album,
                                         like_total=45,
                                         owner="Onur",
                                         )
        new_photo.save()
        self.assertEqual(new_photo.owner,"Onur")

