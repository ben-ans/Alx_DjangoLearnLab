from django.urls import path
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns =[
    path('books/', views.list_books_view, name='books'),
    path('books/<library_name>/', views.LibBooks.as_view(), name='list_lib_books'),
    path('accounts/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]