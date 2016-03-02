#!/home/hunce/VirtualEnv/Assignment/bin/python
from AlbumCreator.views import fetch_photos, check_sending_mail_condition
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        fetch_photos()
        check_sending_mail_condition()
