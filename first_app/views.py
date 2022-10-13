from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def index(request):
    return Response({
        'status': 200,
        'msg' : 'yes working'
    })