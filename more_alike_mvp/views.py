from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Odell Purifoy',
        'title' : 'First Post',
        'content' : 'First Post Content',
        'date_posted' : 'November 16, 2020'
    },
    {
        'author' : 'Amare Purifoy',
        'title' : 'Second Post',
        'content' : 'Second Post Content',
        'date_posted' : 'September 17, 2020'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'more_alike_mvp/home.html', context)


def about(request):
    return render(request, 'more_alike_mvp/about.html', {'title' : 'More Alike (About)'})
