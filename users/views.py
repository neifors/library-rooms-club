from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
# Create your views here.

def signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            req.session['email'] = form.cleaned_data.get('email')
            # messages.success(req, f'Welcome, {username}!')
            return redirect('email')
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, "users/signup.html", data)
