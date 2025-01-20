from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # تحديد الحقول التي تظهر في واجهة الإدارة
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # حذف الإشارة إلى 'username' و 'first_name' و 'last_name'
    list_display = ('email', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
