from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomCreationForm, ConditionForm
from .models import CustomUser



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
      person  = CustomUser.objects.get(username = request.user.username)     
      if person.is_superuser:
        messages.success(request, f"user {username} successfully logged in")
        return redirect(docView)
      messages.success(request, f"user {username} successfully logged in")
      return redirect(home)
  return render(request, 'auth/login.html', {'form': form})


def home(request):
  return render(request, 'main/home.html')


def docView(request):
   return render(request, 'main/doctor.html')


def calls(request): 
  if request.method == 'POST':
       form = ConditionForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,  "Response Recorded. You will receive an email with the full details instructions")
          return redirect('home')
  else:
     form = ConditionForm()
  return render(request, 'main/book.html', {'form': form})
