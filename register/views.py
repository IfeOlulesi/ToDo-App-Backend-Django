from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      print('Form is valid')
      form.save()
      return redirect('/todo')
  else:
    form = RegisterForm()
    
  return render(request, "register/register.html", {"form":form})