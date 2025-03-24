from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('teacher/dashboard/', views.teacher_dashboard_view, name='teacher_dashboard'),
    path('teacher/add_student/', views.add_student_view, name='add_student'),
    path('teacher/delete_student/<int:student_id>/', views.delete_student_view, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
]