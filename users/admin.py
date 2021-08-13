from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'name',)
    list_filter = ('is_superuser', 'is_staff')
    ordering = ('-start_date',)
    list_display = (
        'name',
        'email',
        'is_superuser',
        'is_staff',
    )
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            )}
         ),
    )
    filter_horizontal = ([
        'groups',
        'user_permissions',
    ])


admin.site.register(
    User,
    UserAdminConfig
)

