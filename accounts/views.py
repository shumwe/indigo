from django.shortcuts import render, redirect
from accounts.forms import ProfileUpdateForm, UserUpdateForm
from core.models import Tutorial
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def profile(request, username):
    context = {}
    user = User.objects.get(username=username)
    context['owner'] = user
    if user == request.user:
        is_owner = True
    else:
        is_owner = False
    context['is_owner'] = is_owner
    tutorials = Tutorial.objects.filter(author=user)
    context['tutorials'] = tutorials
    if tutorials:
        for tutorial in tutorials:
            if tutorial.author == user:
                allow_edit = True
            else:
                allow_edit = False
        context['allow_edit'] = allow_edit

    latest_5 = tutorials[:5]
    context['latest_5'] = latest_5
    get_viewset = tutorials.values('hit_count_generic__hits')
    total_views = sum(item['hit_count_generic__hits'] for item in get_viewset)
    context['total_views'] = total_views
    return render(request, 'accounts/profile.html', context)

@login_required
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