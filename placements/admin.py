from django.contrib import admin
from .models import Batch, StudentProfile, TeacherProfile

admin.site.register(Batch)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)