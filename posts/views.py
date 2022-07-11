from django.shortcuts import get_object_or_404, render
from django.views import generic
from posts.models import Category, Posts


# Create your views here.

class CategoryListView(generic.ListView):
    template_name = 'blog/pages/categorys.html'
    model = Category
    paginate_by = 5
    context_object_name = 'kategori'


class CategoryView(generic.ListView):
    template_name = 'blog/pages/kategori.html'
    context_object_name = 'kategori'
    paginate_by = 3

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.gönderi.all()


class PostView(generic.DetailView):
    template_name = 'blog/pages/detail.html'
    model = Posts
    context_object_name = 'post'
