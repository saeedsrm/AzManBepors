from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Responder


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display_links = (
        'first_name', 'last_name', 'username', 'phone_number', 'is_active', 'date_joined', 'email',)
    list_display = (
        'first_name', 'last_name', 'username', 'phone_number', 'is_active', 'date_joined', 'email',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'fullname', 'first_name', 'last_name', 'username', 'phone_number', 'email', 'collage', 'student_code',
                'city', 'province', 'entering_year',
                'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# class ResponderUserAdmin(UserAdmin):
#     model = Responder
#     list_display_links = ('user.fullname'
#                           )
#     list_display = (
#         'user.fullname',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Responder)
