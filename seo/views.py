from django.shortcuts import render, redirect
from .forms import *
from .models import Blog
from django.views.generic import ListView

def Home(request):
    return render(request, template_name='seo/index.html')

def Aboutus(request):
    return render(request, template_name='seo/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
    return render(request, template_name='seo/contact.html', context=context)

def service(request):
    return render(request, template_name='seo/service.html')
# Create your views here.

# def blog_list(request):
#     blog_list = Blog.objects.all()
#     context = {
#         'blog-list': blog_list
#     }
#     return render(
#         request,
#         template_name='seo/blog.html',
#         context=context
#     )
def blog_list(request):
    posts = Blog.objects.all()
    context = {'posts':posts}
    return render(request, template_name='seo/blog.html', context=context)
