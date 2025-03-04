from django.urls import path
from .views import landing_page, home, contact_page

urlpatterns = [
    path('', landing_page, name='landing'),  # First landing page before login
    path('home/', home, name='home'),  # Home page after login
    path('contact/',contact_page,name='contact'),
]
