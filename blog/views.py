from django.shortcuts import render
from blog.models import About, Cover, Social, Inbox, Titles, Contact

# Create your views here.
def index(request):
    covers = Cover.objects.all()
    posts = Posts.objects.all().order_by('-id')
    return render(request, 'home/index.html', {'covers': covers, 'posts': posts})