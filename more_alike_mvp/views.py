from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'more_alike_mvp/home.html', context)


def about(request):
    return render(request, 'more_alike_mvp/about.html', {'title' : 'More Alike (About)'})
