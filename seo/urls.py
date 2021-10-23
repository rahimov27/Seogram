from django.urls import path
from .views import *
from django.conf.urls.static import static
from Seogram import settings


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post-detail/<str:slug>', PostDetail.as_view(), name='post-detail'),
    path('about/',aboutus,name='about'),
    path('blog_list/',blog_list,name='blog-list'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('category/<str:slug>', get_category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)