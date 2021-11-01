from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .forms import *
from .models import Blog, Category 
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from Seogram.settings import *
from django.contrib import messages



def send_mail_test(request):
    if request.method == 'POST':
        form = ContactFormTest(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form .cleaned_data['content'],
                'gurbaali21@gmail.com',
                ['kayratsagynbekov@gmail.com'],
                fail_silently=True
            )
            if mail:
                messages.success(request,'Письмо успешно отправлено')
                return redirect('/')
            else:
                messages.error(request,'Ошибка отправки')
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        form = ContactFormTest
    return render(
        request,
        'seo/test_mail.html',
        {'form':form}
    )

# def login(request):
#     return render(request, 'seo/login.html')

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context = {'form': form, 'categories': categories}
        return render(request, 'seo/login.html', context)
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'seo/login.html', {'form': form})






def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'seo/register.html',
                {'new_user': new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'seo/register.html',
        {'user_form': user_form}
    )





class Home(ListView):
    model = Blog
    template_name = 'seo/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Blog'
        return context

class Blog_list(ListView):
    model = Blog,Category
    template_name = 'seo/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            'posts': Blog.objects.order_by('title'),
            'category': Category.objects.all(),
        })
        return context

    def get_queryset(self):
        return Blog.objects.order_by('title')


class Blog_Detail(DetailView):
    model = Blog
    template_name = 'seo/blog-details.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self,*, object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchResultsView(ListView):
    model = Blog
    template_name = 'seo/search.html'
    context_object_name = 'post'
    paginate_by = 3
    def get_context_data(self,*, object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list

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



def sent(request):
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
    return render(request, template_name='seo/sent.html', context=context)

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


class SearchResult(ListView):
    model = Category
    template_name = 'seo/category.html'
    context_object_name = 'post'
    paginate_by = 3
    def get_context_data(self,*, object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Category.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
        return object_list