from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_mail , name='my_mail')
]
