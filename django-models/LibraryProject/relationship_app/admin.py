from django.contrib import admin
from .models import Author,Book,Library,Libarian

# Register your models here.
# AUTHOR NAME
class AdminAuthor(admin.ModelAdmin):
    list_display = ('name',)

# BOOKS IN THE LIBRARY
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author')

#
class AdminLibrary(admin.ModelAdmin):
    list_display = ('name', 'list_books')

    def list_books(self, obj):
        return  ",".join([book.title for book in obj.books.all()])
    
    list_books.short_description = 'Books'

#
class AdminLibarian(admin.ModelAdmin):
    list_display = ('name', 'library')

admin.site.register(Libarian, AdminLibarian)
admin.site.register(Author, AdminAuthor)
admin.site.register(Book, AdminBook)
admin.site.register(Library, AdminLibrary)