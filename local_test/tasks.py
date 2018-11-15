from __future__ import absolute_import, unicode_literals

import time

from local import celery_app


@celery_app.task
def check_order_pay_time(obj):
    print('开始及时')
    ss = obj.__len__()
    time.sleep(obj.__len__())
    print('%s已经过了' % ss)
    print('订单已经失效')
