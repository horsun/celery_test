```
###################
# 在总conf中添加这个就能在线启动celery任务
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
