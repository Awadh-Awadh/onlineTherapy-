from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomCreationForm


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
  form = AuthenticationForm()
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username = username, password = password)
      if user is not None:
          login(request, user)
          if user.is_superuser:
              return redirect(doc_view)
          return redirect(home)    
  return render(request, 'auth/login.html', {'form':form})


def home(request):
  return render(request, 'main/home.html')


def doc_view(request):
  ...