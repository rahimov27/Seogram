from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name='home'),
    path('about/',Aboutus,name='about'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
]