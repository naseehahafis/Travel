from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name='RIYA'
    return render(request,"index.html",{'obj':name})
def addition(request):
     n1=int(request.GET['num1'])
     n2=int(request.GET['num2'])
     res=n1+n2
     return render(request,"result.html",{'result':res})
