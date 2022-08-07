from django.shortcuts import render


# Create your views here.
def megan(request):
    return render(request,'mega/megan.html')
def prettymegan(request):
    return render(request,'mega/prettymegan.html')
def g2048(request):
    return render(request,'mega/index.html')