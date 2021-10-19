from django.shortcuts import render

def Home(request):
    return render(request,template_name='seo/index.html')

def Aboutus(request):
    return render(request,template_name='seo/about.html')

def blog(request):
    return render(request,template_name='seo/blog.html')
def contact(request):
    return  render(request,template_name='seo/contact.html')
def service(request):
    return render(request, template_name='seo/service.html')
# Create your views here.
