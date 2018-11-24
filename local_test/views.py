# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from local import celery_app
from .tasks import check_order_pay_time


class HAha(APIView):
    def get(self, request):
        x = 100
        out = [x for x in range(x)]
        task = check_order_pay_time.delay(out)
        print(task.id)
        print('sleep:%s' % out.__len__())
        return Response(task.id, status.HTTP_200_OK)


class Stop(APIView):
    def get(self, request, task_id):
        celery_app.control.revoke(task_id, terminate=True)
        return Response('success', status.HTTP_200_OK)
