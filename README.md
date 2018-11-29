```
###################
# 在总conf中添加这个就能在线启动celery 的web 管理工具
#[inet_http_server]
#port=*:9001
#username=admin
#password=admin123
###################
sudo apt install supervisor  或者yum install supervisor
sudo cp ./celery_back.conf  /etc/supervisor/conf.d
$ sudo supervisorctl reread
$ sudo supervisorctl update
$ sudo supervisorctl start celery_worker   还有/restart/ stop /
$ sudo supervisorctl status
celery_worker                    RUNNING   pid 16751, uptime 0:00:34
```


>[教程](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html)

```
在实际项目中可能还有用到延迟队列，比如 n分钟后关闭订单
需要将delay()方法改为apply_async((*args),countdown=n*60), countdown 单位是秒
详细见
```
 [文档](http://docs.celeryproject.org/en/master/userguide/calling.html#eta-and-countdown)