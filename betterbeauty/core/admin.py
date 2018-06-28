from custom_user.admin import EmailUserAdmin

from django.contrib import admin

from core.models import User


class UserAdmin(EmailUserAdmin):
    list_display = ('__str__', 'email', 'role', 'is_superuser', 'date_joined',
                    'is_active',)
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', )
    search_fields = ('email', 'first_name', 'last_name', 'phone', )

    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'first_name', 'last_name', 'phone', 'photo'
        )}),
        ('Permissions', {'fields': ('is_active', 'role', 'is_staff', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'photo'
            )
        }),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser',)})
    )


admin.site.register(User, UserAdmin)
