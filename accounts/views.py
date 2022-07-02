from django.shortcuts import render, redirect
from core.models import Tutorial
from django.contrib.auth import get_user_model
User = get_user_model()

def profile(request, username):
    user = User.objects.get(username=username)
    if user == request.user:
        is_owner = True
    else:
        is_owner = False
    tutorials = Tutorial.objects.filter(author=user)[:5]
    
    context = {'owner': user, 'is_owner': is_owner, 'tutorials': tutorials}
    return render(request, 'accounts/profile.html', context)
