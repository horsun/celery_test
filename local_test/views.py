# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from local import celery_app
from .tasks import check_order_pay_time, create_random_user_accounts


class CreateTimedTask(APIView):
    def get(self, request):
        """
        create a Timed task
        :param request:
        :return:
        """
        x = 100
        out = [x for x in range(x)]
        task = check_order_pay_time.delay(out)
        print(task.id)
        print('sleep:%s' % out.__len__())
        return Response(task.id, status.HTTP_200_OK)


class Stop(APIView):
    def post(self, request, task_id):
        """
        before time end ,end the task

        :param request:
        :param task_id:
        :return:
        """
        celery_app.control.revoke(task_id, terminate=True)
        return Response('success', status.HTTP_200_OK)


class GenerateRandomUserView(APIView):

    def get(self, request):
        total = request.query_params.get('total', 50)
        task = create_random_user_accounts.delay(int(total))
        print(task.id)
        return Response('request has get, and response first', status.HTTP_200_OK)
