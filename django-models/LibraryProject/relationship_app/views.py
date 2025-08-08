from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from .models import Book, Library
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required




# Create your views here.
def list_books_view(request):
    books = Book.objects.select_related('author').all()
        
    return render(request,'relationship_app/list_books.html', {"books": books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('books')
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        book.save()
        return redirect('books')
    return render(request, 'relationship_app/edit_book.html', {'book':book})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'relationship_app/delete_book.html', {'book':book})


class LibBooks(ListView):
    model = Book
    template_name = "relationship_app/list_lib_books.html"
    # context_object_name

    def get_queryset(self):
        self.library = get_object_or_404(Library,
            name__iexact=self.kwargs["library_name"]   # case-insensitive match
        )
  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = self.library
        return context



# AUTHENTICATION PART
def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('books')
        else:
            messages.success(request, ("There was a problem in your logins please try again"))
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})
    
def logout_user(request):
    logout(request)
    return render(request,'registration/logout.html')


def register_user(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration was successful"))
    else:
        return render(request, 'registration/register_user.html', {} )