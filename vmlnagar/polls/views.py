from django.shortcuts import render

# Create your views here.

def pollIndex(request):
    return render(request,"blog/index.html",{})
