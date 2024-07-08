from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                raw_password = form.cleaned_data['password']
                user = authenticate(username=username, password=raw_password) 
                if user is not None: 
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect('musician_list')
        
        else: 
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('musician_list')


def user_logout(request):
    logout(request)
    messages.warning(request, "Logged Out Successfully")
    return redirect('login_page')