from django.shortcuts import render
from blog.models import About, Cover, Social, Inbox, Titles, Contact
from posts.models import Posts, Category
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from blog.forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def home(request):
    covers = Cover.objects.all()
    posts = Posts.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'covers': covers, 'posts': posts})


def about(request):
    about = About.objects.all()
    return render(request, 'blog/pages/about.html', {'about': about})


class ContactView(generic.CreateView, SuccessMessageMixin):
    form_class = ContactForm
    template_name = 'blog/pages/contact.html'
    model = Contact
    context_object_name = 'iletisim'
    success_url = reverse_lazy('contact')
    success_message = 'Mesajınız iletildi'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, self.success_message)
        return super(ContactView, self).form_valid(form)
