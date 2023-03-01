from django.urls import path
from . import views

urlpatterns = [
    path('', views.hook_receiver, name = 'hook_receiver'),
]