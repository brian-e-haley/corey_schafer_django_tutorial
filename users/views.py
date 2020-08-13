from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect)

from .forms import (
    ProfileUpdateForm,
    UserRegisterForm,
    UserUpdateForm)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Your account has been created! You are now able to log in '
                f'{username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/register.html',
        {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        profile_update_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        user_update_form = UserUpdateForm(
            request.POST,
            instance=request.user)
        if profile_update_form.is_valid() and user_update_form.is_valid():
            profile_update_form.save()
            user_update_form.save()
            messages.success(
                request,
                f'Your account has been updated!')
            return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
        user_update_form = UserUpdateForm(instance=request.user)
    context = {
        'profile_update_form': profile_update_form,
        'user_update_form': user_update_form}

    return render(
        request,
        'users/profile.html', context)
