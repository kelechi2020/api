from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Belema
from .serializers import BelemaSerializer

#/stock/
class BelemaList(APIView):

    def get(self, request):
        belema = Belema.objects.all()
        serializer = BelemaSerializer(belema, many=True)
        return Response(serializer.data)


    def post(self, request):
        pass
