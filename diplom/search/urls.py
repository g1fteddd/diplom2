from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('items/', search, name='items'),
    path('<int:pk>/', detail, name='detail')
]