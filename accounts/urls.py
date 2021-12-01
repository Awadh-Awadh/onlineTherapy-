from django.urls import path
from .views import landing, log, home, docView, reg

urlpatterns = [
   path('', landing, name='landingpage'),
   path('login/', log, name = 'login'),
   path('register/', reg, name='register'),
   path('home/', home, name = 'home'),
   path('doctordata/', docView, name = 'docView'),

]