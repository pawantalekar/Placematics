from django.shortcuts import render
from .models import PlacedStudent

def placed_students(request):
    students = PlacedStudent.objects.all()
    return render(request, 'placements/placed_students.html', {'students': students})
