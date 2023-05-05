from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts =[
    {
        'author': 'Prashant',
        'title': 'My First django webapp',
        'content': 'Creating Blog Page',
        'date_posted': 'May 3, 2023'            
    },
    {
        'author':'Aman',
        'title':'KIET College',
        'content':'Review',
        'date_posted':'May 2, 2023'            
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})


