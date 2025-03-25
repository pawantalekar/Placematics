# placements/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('teacher/', views.teacher_dashboard_view, name='teacher_dashboard'),
    path('teacher/add-student/', views.add_student_view, name='add_student'),
    path('teacher/delete-student/<int:student_id>/', views.delete_student_view, name='delete_student'),
    path('teacher/student/<int:student_id>/', views.student_profile_view, name='student_profile'),  # New URL
]