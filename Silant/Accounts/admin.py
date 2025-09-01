from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'groups_list')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email')

    def groups_list(self, obj):
        return ", ".join([g.name for g in obj.groups.all()])
    groups_list.short_description = 'Группы'

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'groups')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)