from django.urls import path
from .views import *
from django.conf.urls.static import static
from Seogram import settings


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post-detail/<str:slug>', Blog_Detail.as_view(), name='post-detail'),
    path('about/',Aboutus.as_view(),name='about'),
    path('blog_list/',Blog_list.as_view(),name='blog-list'),
    path('contact/',contact,name='contact'),
    path('service/',Service.as_view(),name='service'),
    path('category/<str:slug>', get_category, name='category'),
    path('sent/<int:pk>',sent,name = 'sent'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)