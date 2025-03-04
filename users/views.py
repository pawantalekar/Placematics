# users/views.py
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Logs the user out
    return redirect('landing')  # Redirect to index.html after logout


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
