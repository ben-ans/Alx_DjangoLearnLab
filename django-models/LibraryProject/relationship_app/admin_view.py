from  django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import UserProfile


def is_admin(user):
    return hasattr(user, 'userprofile') and UserProfile.role == 'Admin'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})
