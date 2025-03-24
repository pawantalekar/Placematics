from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    year = models.IntegerField(unique=True)
    def __str__(self):
        return f"Batch {self.year}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    tenth_percent = models.FloatField(blank=True, null=True)
    twelfth_percent = models.FloatField(blank=True, null=True)
    graduation_percent = models.FloatField(blank=True, null=True)
    placement_status = models.CharField(
        max_length=20,
        choices=[('Placed', 'Placed'), ('Unplaced', 'Unplaced'), ('In Progress', 'In Progress')],
        default='Unplaced'
    )
    package = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.user.username

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username