
from django.urls import path, include
from django.views import generic
from . import views

app_name = 'profile'

urlpatterns = [
    path('<int:pk>/<str:user>/', views.ProfileView.as_view(), name='home'),
    path('basic-update/', views.BasicProfileUpdate.as_view(), name='basic'),
    path('<int:pk>/<str:user>/detail-update/', views.profile_detail, name='detay'),
]
