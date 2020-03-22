from django.test import TestCase

# Create your tests here.
from django.conf.urls import url
from . import views
from django.urls import path
from placementsportal import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    path(r'sync/<int:pk>/',views.sync,name='sync')

]
