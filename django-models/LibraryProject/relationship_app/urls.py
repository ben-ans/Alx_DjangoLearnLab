from django.urls import path
from .views import list_books_view, LibBooks, login_user, logout_user, register_user
urlpatterns =[
    path('books/', list_books_view, name='books'),
    path('books/<library_name>/', LibBooks.as_view(), name='list_lib_books'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

]