from django.urls import path
from posts import views

urlpatterns = [
    path('<slug>/', views.CategoryView.as_view(), name='kategori'),
    path('<category>/<slug>', views.PostView.as_view(), name='detay'),
]
