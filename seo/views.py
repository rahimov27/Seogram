from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact
def Home(request):
    return render(request,template_name='seo/index.html')

def Aboutus(request):
    return render(request,template_name='seo/about.html')

def blog(request):
    return render(request,template_name='seo/blog.html')
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
    return  render(request,template_name='seo/contact.html',context=context)
def service(request):
    return render(request, template_name='seo/service.html')
# Create your views here.
