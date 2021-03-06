from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomCreationForm, ConditionForm, ProfileUpdate
from .models import Conditions, CustomUser
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required




# Create your views here.


def landing(request):

   return render(request, "main/landing.html")


def reg(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"user {username} successfully created")
            return redirect('login')
    else:
        form = CustomCreationForm(request.POST)
    context = {
      'form':form
    }

    return render(request, 'auth/reg.html', context)

def log(request):
  form = AuthenticationForm(request.POST)
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
      login(request, user)
      person  = CustomUser.objects.get(username = request.user.username)     
      if person.is_superuser:
        messages.success(request, f"user {username} successfully logged in")
        return redirect(docView)
      messages.success(request, f"user {username} successfully logged in")
      return redirect(home)
  return render(request, 'auth/login.html', {'form': form})

@login_required
def home(request):
  return render(request, 'main/home.html')

@login_required
def docView(request):
   conditions = Conditions.objects.all()
   users_count = CustomUser.objects.all().count()
   conditions_count = Conditions.objects.all().count()
   context = {
     'conditions': conditions,
     'users': users_count,
     'bookcount': conditions_count,
   }
   return render(request, 'main/doctor.html', context)


def calls(request): 
  if request.method == 'POST':
       form = ConditionForm(request.POST)
       if form.is_valid():
          obj = form.save(commit=False)
          obj.user = request.user
          obj.save()
          messages.success(request,  "Response Recorded. You will receive an email with the full details instructions.Thank You")
          return redirect('home')
  else:
     form = ConditionForm()
  return render(request, 'main/book.html', {'form': form})

def profile(request):
  if request.method == 'POST':
    form = ProfileUpdate(request.POST, instance=request.user.profile)
    if form.is_valid():
      obj = form.save(commit=False)
      obj.user = request.user
      obj.save()
  else:
    form = ProfileUpdate()
  context = {
    'form': form
  }
  return render(request, 'main/profile.html', context)


def approve(request):
  return render(request, 'main/email.html')