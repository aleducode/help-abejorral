"""User models admin"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from abjhelp.users.models import User, HelpRequest, DonorRequest


class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'created')


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    """Profile model admin"""
    list_display = ('name', 'is_active')
    search_fields = ('name', 'address', 'description')
    list_filter = ('is_active',)

    
@admin.register(DonorRequest)
class DonorRequestAdmin(admin.ModelAdmin):
    """Profile model admin"""
    list_display = ('name', 'is_active',)
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('is_active',)

admin.site.register(User, CustomUserAdmin)
