from django.shortcuts import render
from .permission import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import AllowAny
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
# List view -- to retrieve all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Anyone can list
    filter_backends = [DjangoFilterBackend]
    filter_class = BookFilter

# DetailView to retrieve a book base on  the ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] 

# Generic CreateView to create a new bookk item
class CreateView (generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] 

# Generic UpdateViiew to modify an existing book
class UpdateView (generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Generic DeleteView to remove a book
class DeleteView (generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------Create Author view-----------------
class AuthorCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]  # Anyone can list

# DetailView to retrieve a author base on  the ID
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny] 

# Generic UpdateViiew to modify an existing book
class AuthorUpdateView (generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Generic DeleteView to remove a book
class AuthorDeleteView (generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]