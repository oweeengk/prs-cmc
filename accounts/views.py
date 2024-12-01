from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm

# Create your views here.
def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None and user.groups.filter(name="Faculty").exists():
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid Credentials or Unauthorized Access")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "accounts/login.html", context)

def student_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None and user.groups.filter(name="Students").exists():
                login(request, user)
                return redirect("student_home")
            else:
                messages.error(request, "Invalid Credentials or Unauthorized Access")
                return redirect("student_login")

    context = {
        "forms": forms
    }
    return render(request, "accounts/student_login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

