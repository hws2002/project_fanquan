from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User
# Register your models here

class MyUserAdmin(UserAdmin):
    list_display = ('email','username','is_active','is_staff','is_superuser','user_type')
    list_filter = ('is_active','is_staff','is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password','user_type','name', 'telephone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','password1','password2','user_type','is_active','is_staff','is_superuser','name','telephone'),
        }),
    )
    search_fields = ('email','username','name')
    ordering = ('email',)


admin.site.register(User,MyUserAdmin)
