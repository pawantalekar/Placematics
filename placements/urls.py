from django.urls import path
from . import views

urlpatterns = [
     path('placed-students/', views.placed_students, name='placed_students'),
    path('add-placement/', views.add_placement, name='add_placement'), 
]
