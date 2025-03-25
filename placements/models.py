from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    year = models.IntegerField(unique=True)
    def __str__(self):
        return f"Batch {self.year}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    batch = models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, blank=True)
    placement_status = models.CharField(max_length=20, choices=[('Placed', 'Placed'), ('Unplaced', 'Unplaced'), ('In Progress', 'In Progress')], default='Unplaced')
    
    # New fields
    full_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    tenth_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    twelfth_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    graduation_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    certificates = models.JSONField(default=list, blank=True)  # For storing certificates as a list

    def __str__(self):
        return self.user.username

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username