from django.urls import path
from .views import landing, log, home, doc_view, reg

urlpatterns = [
   path('', landing, name='landingpage'),
   path('login/', log, name = 'login'),
   path('register/', reg, name='register')
]