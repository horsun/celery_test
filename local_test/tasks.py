from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string


@shared_task
def check_order_pay_time(obj):
    ss = obj.__len__()
    print('start sleep %s s' % ss)
    time.sleep(ss)
    print('%s seconds has gone,success' % ss)


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{0}'.format(get_random_string(10, string.ascii_letters))
        email = '{0}@example.com'.format(username)
        pwd = get_random_string(50)
        User.objects.create_user(
            username=username,
            email=email,
            password=pwd,
        )
    return '{0} random users created with success!'.format(total)


@shared_task
def test_sequence(num):
    time.sleep(int(num))
    username = get_random_string(10) + '__' + str(num)
    email = '{0}@example.com'.format(username)
    pwd = get_random_string(50)
    User.objects.create_user(
        username=username,
        email=email,
        password=pwd,
    )
    return '{0}created with success!'.format(username)
