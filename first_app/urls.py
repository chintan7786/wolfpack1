from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('usercheck/', UserCheck.as_view(), name='UserCheck'),
]
