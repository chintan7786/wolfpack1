from django.shortcuts import render
from pkg_resources import require
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


class UserCheck(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Success'}
        return Response(content)



# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'msg' : 'yes working',
            'method' : 'GET'
        })
    elif request.method == 'POST':
        return Response({
            'method': 'POST'
        })
    else:
        return Response({
            'method': 'invalid'
        })
