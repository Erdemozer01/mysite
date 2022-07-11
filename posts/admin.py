from django.contrib import admin
from posts.models import Posts, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created']
    list_filter = ['title', 'author', 'status', 'created']