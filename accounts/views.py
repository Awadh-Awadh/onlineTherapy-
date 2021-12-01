from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomCreationForm
from .models import CustomUser


# Create your views here.


def landing(request):

   return render(request, "main/landing.html")


def reg(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
      person  = CustomUser.objects.get(username = request.user.username)     
      if person.is_superuser:
        return redirect(docView)
      return redirect(home)
  return render(request, 'auth/login.html', {'form': form})


def home(request):
  return render(request, 'main/home.html')


def docView(request):
   return render(request, 'main/doctor.html')