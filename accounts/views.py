from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 

from .forms import UpdateUserForm, UpdateProfileForm
# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST': 
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Yay! Your profile is updated successfully!")
            return redirect(to='users-profile')
    else: 
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)

    return render(request, 'account/profile.html', {'user_form': user_form, 'profile_form': profile_form})

