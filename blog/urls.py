from django.urls import path
from .views import home, create, read, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('post/<int:pk>/', read, name='read'),
    path('post/<int:pk>/update/', update, name='update'),
    path('post/<int:pk>/delete/', delete, name='delete'),
]
