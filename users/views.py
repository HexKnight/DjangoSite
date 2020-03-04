from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"A new user is created for {username}!")
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
