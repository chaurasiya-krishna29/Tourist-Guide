from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contact, Destination



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Fields shown in the user list
    list_display = ('email', 'first_name', 'mobile', 'city', 'date_joined', 'is_active')
    
    # Fields that can be used for filtering
    list_filter = ('is_active', 'date_joined', 'city')
    
    # Fields that can be searched
    search_fields = ('email', 'first_name', 'mobile', 'city')
    
    # Default ordering
    ordering = ('-date_joined',)

    # Remove username from the fieldsets since we're using email
    fieldsets = (
        ('Personal Info', {
            'fields': ('email', 'password', 'first_name', 'mobile', 'city')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Fields shown when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'mobile', 'city', 'password1', 'password2'),
        }),
    )

    # Use email as the unique identifier instead of username
    ordering = ('email',)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at', 'location')