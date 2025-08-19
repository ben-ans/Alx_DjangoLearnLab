from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Creating the books Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publicvation_year','author']
        # fields = __all__

# Validation code to ensure that the publication year is not in the future
# By comparing the year to the current year
    def validate_verification_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year can not be in the future")
        return value


# Code to serialize the Author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# If you query an author endpoint (GET /api/authors/), 
# it will return author and his related books in a json format