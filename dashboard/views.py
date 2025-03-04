from django.shortcuts import render
from placements.models import PlacedStudent
# dashboard/views.py
from django.shortcuts import render
from placements.models import PlacedStudent

def home(request):
    placed_students = PlacedStudent.objects.filter(status='placed')
    return render(request, 'dashboard/home.html', {'placed_students': placed_students})


# Landing page (first page before login)
def landing_page(request):
    return render(request, "dashboard/index.html")

# Home page (showing placed students after login)
def home(request):
    # placed_students = PlacedStudent.objects.all()
    return render(request, "dashboard/home.html")
def contact_page(request):
    return render(request,'dashboard/contact.html')
