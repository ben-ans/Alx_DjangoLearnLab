from  django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CustomUser


def is_librarian(user):
    return hasattr(user, 'userprofile') and CustomUser.role == 'librarian'

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/member_view.html', {})
