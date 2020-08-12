from django.shortcuts import render,HttpResponse

# Create your views here.

def to_indexPage(request):
    return render(request,'index.html')