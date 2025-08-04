import os
import sys
import django

# Add the project root to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author,Book,Library,Libarian

#Query books by a specific author
author_name = "Ben Boddy"
try:
    author = Author.objects.filter(name=author_name)
    books_by_author = Book.objects.filter(authoer = author)
    print(f"Boooks by {author_name}: ")
    for book in books_by_author:
        print(f"{book.title}")

except Author.DoesNotExist:
    print(f"No author is found with name: {author_name}")


#ALl books in the Library
library_name = "Central Library"
try:
    library = Library.objects.filter(name = library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}")
    for book in books_in_library:
        print(f"- {book.title}")

except Library.DoesNotExist:
    print(f"No Library found with the name {library_name}")


#Retrieve the Libarian for a library
try:
    librarian = Libarian.objects.filter(library_name=library_name)
    print(f"\nLibrarian for {library_name} is {librarian.name}")
except Libarian.DoesNotExist:
    print(f"No Librarian is assigned to {library_name}")