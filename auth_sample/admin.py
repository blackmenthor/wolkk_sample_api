from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_sample.models import User


class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        return qs

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'email',
                    'password',
                    'created_date',
                    'first_name',
                    'last_name',
                    'groups'
                )
            }
        ),
        (
            'Permissions',
            {
                'fields':
                    (
                        'is_staff',
                        'is_active',
                        'is_superuser'
                    )
            }
        ),
    )
    readonly_fields = [
        'created_date'
    ]
    add_fieldsets = (
        (
            None,
            {
                'classes':
                    (
                        'wide',
                    ),
                'fields':
                    (
                        'username',
                        'email',
                        'is_staff',
                        'first_name',
                        'last_name',
                        'groups',
                        'created_date'
                    )
            }
        ),
    )


admin.site.register(User, CustomUserAdmin)
