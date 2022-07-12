from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'date_of_birth', 'created']
    list_filter = ['user', 'email']
    search_fields = ['user', 'email']
    raw_id_fields = ['user']

    fieldsets = (
        (None, {
            'fields': (
            'user', 'cover', 'avatar', 'first_name', 'last_name', 'email', 'phone', 'job', 'about', 'date_of_birth')
        }),
        ('Sosyal Medya', {
            'classes': ('collapse ', 'extrapretty'),
            'fields': ('facebook', 'twitter', 'instagram', ),
        }),
    )
