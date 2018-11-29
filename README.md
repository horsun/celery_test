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