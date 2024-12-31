from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'myapps/index.html')

def contact(request):
    return render(request, 'myapps/contact.html')
def services(request):
    return render(request,'myapps/services.html')
def about(request):
    return render(request,'myapps/about.html')
def blog(request):
    return render(request,'myapps/blog.html')
def blog_details(request):
    return render(request,'myapps/blog_details.html')
def testimonials(request):
    return render(request,'myapps/testimonials.html')
def login(request):
    return render(request,'myapps/login.html')
