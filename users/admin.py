from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define the custom user admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    # Define the fields to display on the user form in admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Include the filter options for admin list view
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
