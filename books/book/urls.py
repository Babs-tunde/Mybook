from django.urls import path
from . import views
from .views import register_book, edit_book

urlpatterns = [
    path('register/', views.register_book, name='register_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]
