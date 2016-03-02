# coding=utf-8
from __future__ import absolute_import
from AlbumCreator.views import fetch_photos, authorized_to_twitter, \
     check_sending_mail_condition
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@periodic_task(run_every=crontab(minute='*/20'))
def fetch_photos_every_20_minutes():
    fetch_photos()
    check_sending_mail_condition()