# from django.db import models
# from django.conf import settings  # Use the AUTH_USER_MODEL setting
# from django.utils import timezone

# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     industry = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# class PlacedStudent(models.Model):
#     student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use the custom user model
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     placement_date = models.DateField(default=timezone.now)
#     role = models.CharField(max_length=255)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=255, choices=[('placed', 'Placed'), ('pending', 'Pending')], default='placed')

#     def __str__(self):
#         return f"{self.student.username} - {self.company.name}"

# placements/models.py
from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

def get_default_user():
    """Returns the first user in the database if exists, else None."""
    return User.objects.first().id if User.objects.exists() else None

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# PlacedStudent Model
class PlacedStudent(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        default=get_default_user  # Uses the first available user as default
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Ensure Company exists before referencing it
    placement_date = models.DateField(default=datetime.date.today)
    role = models.CharField(max_length=255, default="Unknown Role")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        default='Pending',
        choices=[('Placed', 'Placed'), ('Pending', 'Pending'), ('Rejected', 'Rejected')]
    )

    def __str__(self):
        return f"{self.student} - {self.company}"
