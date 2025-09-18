from django.shortcuts import render, redirect
from .models import Post

def index(request):
    return render(request, 'damm/index.html')
    
def blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(title=title, body=body)
        return redirect('/')
    posts = Post.objects.all()
    return render(request, 'damm/blog/index.html', {'posts': posts})
