from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def post(request, id):
    pesquisa = BlogPost.objects.get(pk=id)
    context = {'pesquisa':pesquisa}
    return render(request, 'post.html', context)
    