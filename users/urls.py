from django.urls import path
from .views import custom_logout
from django.contrib.auth import views as auth_views

# Add this line to register the 'users' namespace
app_name = "users"  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),  # Using custom logout function
]
