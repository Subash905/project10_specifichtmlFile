from django.urls import path
from app1.views import *
app_name = 'soumya'

urlpatterns = [
    path('hi/',hi,name='hi'),
]