from  django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile


def is_member(user):
    return hasattr(user, 'userprofile') and UserProfile.role == 'member'

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})