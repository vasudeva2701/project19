from django.urls import path
from app2.views import *
app_name='ram'

urlpatterns=[
    path('pushpa/',pushpa,name='pushpa'),
    path('rahul/',rahul,name='rahul'),
]