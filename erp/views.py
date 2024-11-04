from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse("this is firstone")
def base(request):
    return render(request,'erp/base.html')


# Create your views here.
