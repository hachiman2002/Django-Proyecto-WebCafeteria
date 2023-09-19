from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    #devolver un 404 en caso que no encuentre la categoria
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category} )