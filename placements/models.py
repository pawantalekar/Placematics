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
import datetime
from django.db import models

class PlacedStudent(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
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


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

