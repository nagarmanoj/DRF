from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_index(request):
    post = Post.objects.all().order_by('-created_on')
    context = {
        "post":post,
    }
    return render(request,"blog/index.html",context)


def blog_category(request,category):
    post = Post.objcects.filter(category_name_contain=category).order_by('-created_on')
    conext = {
        "category":category,
        "post":post,
    }
    return render(request,'blog/blog_category.html',context)

def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post":post,
    }
    return render(request,"blog/blog_detail.html",context)
