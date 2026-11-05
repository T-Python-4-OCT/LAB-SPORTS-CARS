from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_page(request:HttpRequest):
    
     return render(request,"main/index.html")

    


def trems_view(request:HttpRequest):

    
    return render(request, "main/Trems.html")



