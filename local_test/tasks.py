from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def check_order_pay_time(obj):
    ss = obj.__len__()
    print('start sleep %s s' % ss)
    time.sleep(ss)
    print('%s seconds has gone' % ss)
    print('final success')
