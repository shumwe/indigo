from django.shortcuts import render, redirect
from accounts.forms import ProfileUpdateForm, UserUpdateForm
from core.models import Tutorial
from django.contrib.auth import get_user_model
User = get_user_model()

def profile(request, username):
    user = User.objects.get(username=username)
    if user == request.user:
        is_owner = True
    else:
        is_owner = False
    tutorials = Tutorial.objects.filter(author=user)
    latest_5 = tutorials[:5]
    get_viewset = tutorials.values('hit_count_generic__hits')
    total_views = sum(item['hit_count_generic__hits'] for item in get_viewset)
    
    context = {'tutorials': tutorials, 'owner': user, 'is_owner': is_owner,
               'latest_5': latest_5, 'total_views': total_views}
    return render(request, 'accounts/profile.html', context)

def profile_settings(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('profile', username=request.user.username)
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_update_form, 
        'profile_form': profile_update_form
               }
    return render(request, 'accounts/settings.html', context)