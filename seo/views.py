from django.shortcuts import render, redirect
from .forms import *
from .models import Blog
from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Blog
    template_name = 'seo/index.html'

class BlogList(ListView):
    model = Blog
    template_name = 'seo/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class PostDetail(DetailView):
    model = Blog
    template_name = 'seo/blog-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

def get_category(request, slug):
    return render(request, 'blog/category.html')

def blog_list(request):
    post = Blog.objects.all()
    context = {
        'posts' : post
    }
    return render(request, template_name='seo/blog.html', context=context)

def aboutus(request):
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