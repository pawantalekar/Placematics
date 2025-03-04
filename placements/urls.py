from django.urls import path
from . import views

urlpatterns = [
    path('placed_students/', views.placed_students, name='placed_students'),
]
