from django.urls import path
from . import views

urlpatterns=[
    path('', views.ninjaMenu),
    path('process_money', views.processMoney),
    path('reset', views.reset)
]