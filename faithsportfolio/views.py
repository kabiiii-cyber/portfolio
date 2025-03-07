from django.shortcuts import render

# Create your views here.


def index(request):
  return render(request,'index.html')

def about(request):
  return render(request,'about.html')

def gallery(request):
  return render(request,'gallery.html')

def services(request):
  return render(request,'services.html')

def gallery_single(request):
  return render(request,'gallery-single.html')

def starter(request):
  return render(request,'starter-page.html')

def contacts(request):
  return render(request,'contact.html')


