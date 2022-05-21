
from django.shortcuts import render
from .models import Plot

# Create your views here.


def index(request):
    return render(request,'base.html')

def rent(request):
    return render(request,'listing.html')

def about(request):
    return render(request,'about.html')

def location(request):
    info = Plot.objects.all()
    param ={'info':info}
    return render(request,'deals.html',param)



