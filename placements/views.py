from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PlacedStudent
from .forms import PlacementForm

@login_required
def add_placement(request):
    """Allow users to submit their placement data."""
    if request.method == "POST":
        form = PlacementForm(request.POST)
        if form.is_valid():
            placement = form.save(commit=False)
            placement.student = request.user  # Assign logged-in user as student
            placement.save()
            return redirect('placed_students')  # Redirect to placement listing page
    else:
        form = PlacementForm()
    return render(request, 'placements/add_placement.html', {'form': form})

@login_required
def placed_students(request):
    """Fetch and display all placed students."""
    students = PlacedStudent.objects.all()
    return render(request, 'placements/placed_students.html', {'students': students})
