from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extended',
            {
                'fields': (
                    'phone', 'bio', 'my_signature', 'location',
                ),
            },
        ),
    )