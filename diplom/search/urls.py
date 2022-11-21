from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list/', upload_file, name='list')
]