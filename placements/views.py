from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudentProfile, TeacherProfile, Batch

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if TeacherProfile.objects.filter(user=user).exists():
                return redirect('teacher_dashboard')
            else:
                return redirect('dashboard')
    return render(request, 'Placements/login.html')

@login_required
def dashboard_view(request):
    if TeacherProfile.objects.filter(user=request.user).exists():
        return redirect('teacher_dashboard')
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'Placements/dashboard.html', {'profile': profile})

@login_required
def profile_view(request):
    profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.tenth_percent = request.POST.get('tenth', None)
        profile.twelfth_percent = request.POST.get('twelfth', None)
        profile.graduation_percent = request.POST.get('graduation', None)
        profile.save()
        return redirect('dashboard')
    return render(request, 'Placements/profile.html', {'profile': profile})

@login_required
def analytics_view(request):
    # Get filter from GET parameters
    status_filter = request.GET.get('status', '')
    
    # Filter students based on status
    if status_filter:
        students = StudentProfile.objects.filter(placement_status=status_filter)
    else:
        students = StudentProfile.objects.all()
    
    # Calculate counts for the chart
    placed = StudentProfile.objects.filter(placement_status='Placed').count()
    unplaced = StudentProfile.objects.filter(placement_status='Unplaced').count()
    in_progress = StudentProfile.objects.filter(placement_status='In Progress').count()
    
    context = {
        'students': students,
        'placed': placed,
        'unplaced': unplaced,
        'in_progress': in_progress,
        'status': status_filter  # For template to display current filter
    }
    return render(request, 'placements/analytics.html', context)

@login_required
def teacher_dashboard_view(request):
    if not TeacherProfile.objects.filter(user=request.user).exists():
        return redirect('dashboard')
    students = StudentProfile.objects.all()
    batches = Batch.objects.all()
    return render(request, 'Placements/teacher_dashboard.html', {'students': students, 'batches': batches})

@login_required
def add_student_view(request):
    if not TeacherProfile.objects.filter(user=request.user).exists():
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        batch_id = request.POST['batch']
        batch = Batch.objects.get(id=batch_id)
        user = User.objects.create_user(username=username, password=password)
        StudentProfile.objects.create(user=user, batch=batch)
        return redirect('teacher_dashboard')
    return redirect('teacher_dashboard')

@login_required
def delete_student_view(request, student_id):
    if not TeacherProfile.objects.filter(user=request.user).exists():
        return redirect('dashboard')
    student = get_object_or_404(StudentProfile, id=student_id)
    user = student.user
    student.delete()
    user.delete()
    return redirect('teacher_dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')