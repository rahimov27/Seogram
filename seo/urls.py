from django.urls import path
from .views import *
from django.conf.urls.static import static
from Seogram import settings
urlpatterns = [
    path('',Home,name='home'),
    path('about/',Aboutus,name='about'),
    path('blog-list/',blog_list,name='blog-list'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)