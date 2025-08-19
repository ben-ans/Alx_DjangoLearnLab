import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # case-insensitive contains
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'publication_year']
