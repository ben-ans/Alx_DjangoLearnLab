from django.urls import path
from .views import list_books_view, LibBooks, login_user, logout_user, register_user
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns =[
    path('books/', list_books_view, name='books'),
    path('books/<library_name>/', LibBooks.as_view(), name='list_lib_books'),
    path('accounts/login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view')
]