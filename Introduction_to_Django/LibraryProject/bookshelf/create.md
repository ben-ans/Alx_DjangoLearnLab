Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32

# after opening the manage.py shell, Import the Books model
>>> from bookshelf.models import Books
>>> Books.objects.all()
<QuerySet []>

# This command creates two objects in the Books models
    Books.objects.create(title="Introduction to Python", author="Ben Boddy", publication_year=2007)
IndentationError: unexpected indent
>>> Books.objects.create(title="Introduction to Python", author="Ben Boddy", publication_year=2007)
<Books: Books object (1)>
>>> Books.objects.create(title="Introduction to Django", author="Boss Ricky", publication_year=2007)
<Books: Books object (2)>

# THIS COMMAND SELECT ALL *
>>> Books.objects.all()                                
<QuerySet [<Books: Books object (1)>, <Books: Books object (2)>]>

# CREATE TO STORE THE SECOND OBJECT
>>> book = Books.objects.get(id=2)
>>> book
<Books: Books object (2)>

# PRINT(READ) THE AUTHOR AND THE PUBLICATION YEAR TO CONFIRM
>>> book.author
'Boss Ricky'
>>> book.publication_year
2007

# UPDATE THE PUBLICATION YEAR
>>> book.publication_year = 2020
>>> book.save()
>>> book.publication_year
2020

# DELETE THE BOOK
>>> book.delete()
(1, {'bookshelf.Books': 1})
>>> Books.objects.all()
<QuerySet [<Books: Books object (1)>]>
>>>
