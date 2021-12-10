from django.urls import path
from .views import landing, log, home, docView, reg, calls, profile, approve
from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('', landing, name='landingpage'),
   path('login/', log, name = 'login'),
   path('register/', reg, name='register'),
   path('home/', home, name = 'home'),
   path('doctordata/', docView, name = 'docView'),
   path('schedule/', calls, name = 'schedule' ),
   path('profile/', profile, name = 'profile' ),
   path('logout/', LogoutView.as_view(template_name = 'main/landing.html'), name = 'logout' ),
   path('email/', approve, name = 'approve')
]