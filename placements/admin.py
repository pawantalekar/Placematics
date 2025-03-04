# from django.contrib import admin
# from .models import PlacedStudent, Company
# from django.contrib import admin
# from .models import StudentPlacement, Company  # Ensure you import the correct model name

# admin.site.register(StudentPlacement)
# admin.site.register(Company)


# class PlacedStudentAdmin(admin.ModelAdmin):
#     list_display = ['student', 'company', 'placement_date', 'role', 'salary', 'status']
#     search_fields = ['student__username', 'company__name', 'role']
#     list_filter = ['status', 'placement_date']

# admin.site.register(PlacedStudent, PlacedStudentAdmin)
# admin.site.register(Company)

from django.contrib import admin
from .models import PlacedStudent, Company  # Corrected import

class PlacedStudentAdmin(admin.ModelAdmin):
    list_display = ['student', 'company', 'placement_date', 'role', 'salary', 'status']
    search_fields = ['student', 'company__name', 'role']
    list_filter = ['status', 'placement_date']

admin.site.register(PlacedStudent, PlacedStudentAdmin)
admin.site.register(Company)
