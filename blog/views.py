from django.shortcuts import render
from blog.models import About, Cover, Social, Inbox, Titles, Contact
from posts.models import Posts, Category


# Create your views here.
def home(request):
    covers = Cover.objects.all()
    posts = Posts.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'covers': covers, 'posts': posts})
