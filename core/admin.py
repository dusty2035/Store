from django.contrib import admin
from .models import CustomUser
# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'is_active']
    list_editable = ['is_active']
    search_fields = ['last_name', 'first_name', 'email', 'phone_number']
    list_display_links = ['email', 'first_name', 'last_name']

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'password')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address', 'postal_code')
        })
    )