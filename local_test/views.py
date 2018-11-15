# Create your views here.
import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import check_order_pay_time


class HAha(APIView):
    def get(self, request):
        x = random.randint(0, 10)
        out = [x for x in range(x)]
        check_order_pay_time.delay(out)
        return Response(out, status.HTTP_200_OK)
