from django.shortcuts import render, redirect
from .forms import *
from .models import Blog
from django.views.generic import ListView,DetailView

class Home(ListView):
    model = Blog
    template_name = 'seo/index.html'

class Blog_list(ListView):
    model = Blog
    template_name = 'seo/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Blog'
        return context


class Blog_Detail(DetailView):
    model = Blog
    template_name = 'seo/blog-details.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'post'
        return context

class Service(ListView):
    model = Blog
    template_name = 'seo/service.html'

class Aboutus(ListView):
    model = Blog
    template_name = 'seo/about.html'

def get_category(request,slug):
    return render(request,'seo/category.html')

# class Contact(request,ListView):
#     model = ContactForm
#     template_name = 'seo/contact.html'
#     context_object_name = 'form'
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = ContactForm()
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['first_name'] = 'Bakyt'
#         return context

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