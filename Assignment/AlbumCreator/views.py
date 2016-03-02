# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from .models import Album, Photo
import tweepy
from tweepy import OAuthHandler
from requests.exceptions import ConnectionError
from facepy import GraphAPI


"""
Authentication for twitter is provided by tweepy.
"""


def authorized_to_twitter():
    try:
        consumer_key = 'gd1MzidvrbnDCu4LmQnQTxXah'
        consumer_secret = '29b5NrProjdYOpLL4eKL00EUy1nR7BCup2Dik6rp3y5PA7IHuq'
        access_token = '703590915143802880-nJJzLRK3GWUL3mLqFQYEwD6uUZnQJlU'
        access_secret = 'UryNGZNkRaQCebkU6qQD6Kllie5BQ5VGUSr3gdb4LmuJo'
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
    except ConnectionError as e:
        print e

    return tweepy.API(auth)


"""
Fetches media images for a given hashtag. Creates new objects for every unique
photo in model. Keeps name of the owner and retweet number for each photo.
"""


def fetch_photos():
    try:
        twitter_api = authorized_to_twitter()
    except ConnectionError as e:
        print e

    # variables
    owner_list = []
    popularity_count = []
    media_files = set()
    list_counter = 0
    album_instance, created = Album.objects.get_or_create(name="Carnival",
                                                          album_capacity=501)
    """
    Tweets with carnival hashtag are fetched. Fetched tweet items
    per time is decided as 50 since twitter does not allow huge amount
    fetch consecutively.
    """
    carnival_tweets = tweepy.Cursor(
        twitter_api.search, q='#carnival').items(50)

    """
    Tweets with media are identified. Url name, owner, and like total
    lists are created.
    """
    for status in carnival_tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            owner_list.append(status.user.name)
            popularity_count.append(status.retweet_count)
            media_files.add(media[0]['media_url'])

    # New objects are created in model for new photos.
    for media_file in media_files:
        print media_file
        if not Photo.objects.filter(url_name=media_file).exists():
            new_photo = Photo.objects.create(
                url_name=media_file, album=album_instance,
                owner=owner_list[list_counter],
                like_total=popularity_count[list_counter]
            )
            new_photo.save()
        list_counter += 1

"""
I optionally created manual option to fetch photos from Twitter.
"""


def fetch_photos_manually_from_browser(request):
    fetch_photos()
    check_sending_mail_condition()

    return redirect("/")


"""
Checks whether total amount of photos are reached to sending a mail condition.
"""


def check_sending_mail_condition():
    total_photo_amount = Photo.objects.filter(
                         album__name="Carnival").count()
    main_album = Album.objects.get(name="Carnival")

    if total_photo_amount <= main_album.album_capacity and \
       total_photo_amount % 100 == 0 and \
       total_photo_amount != 0:
        inform_mail = EmailMultiAlternatives("#carnival has" + str
                                             (total_photo_amount) + "photos",
                                             "I’m awesome!",
                                             "Hashtag@EversnapApp.com",
                                             ["onurhunce@yahoo.com"],
                                             bcc=["davide@geteversnap.com"])
        inform_mail.send()


"""
Retrieves all images from the model.
"""


def get_all_images_from_database(request):
    image_list = Photo.get_all_photos()
    return render(request, "AlbumCreator/photos.html", {"images": image_list})


"""
Retrieves most popular images from the list.
"""


def get_most_popular_photos():
    order_of_popularity = Photo.objects.all().order_by('like_total')
    return order_of_popularity.reverse()[:7]


"""
Shows most popular 7 photos in new page.
"""


def show_popular_photos(request):
    most_popular_photos = get_most_popular_photos()

    return render(request, "AlbumCreator/popular.html", {
        "popular_photos": most_popular_photos})


"""
Authentication for Facebook api is provided. Access token is taken.
"""


def connect_to_facebook():
    try:
        cfg = {
                "access_token": "CAAQV3vigQEgBAFNBgeI0b0jNhinI9WtbkhrsNrD8dP"
                                "A53ym78ouYobZCzUvTIY4IeXcDJB4TAK00s3sjNTv6"
                                "vGJxgyPbT27VantHU8oiXZB9Qbu9azp6Px0r7ZBxZB"
                                "uGbDp0KopHVGdwvYeLJ05u4mrmJnFO64OYoSaj8PID"
                                "j8PZBai2VPcjVgFWCQaThUSFZBMZANTsNnDYwZDZD"
                }
        graph = GraphAPI(cfg['access_token'])
        return graph

    except ConnectionError as e:
        print e


"""
Downloads most popular photos and posts a photo album to Facebook. Silence
pass is explicitly used since short-lived or long-lived authentication
will be a problem for other users. The error code is 1] An unknown error
has occurred. Fake Facebook is used to share albums.
"""


def post_photos_to_facebook(request):

    popular_images = get_most_popular_photos()
    try:
        facebook_wall = connect_to_facebook()
        for photo in popular_images:
            facebook_wall.post(
                path='me/photos',
                url=(photo.url_name, 'rb')
                            )
    except:
        pass

    return redirect("/..")
