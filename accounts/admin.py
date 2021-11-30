from django.contrib import admin
from .models import CustomUser, Profile, Conditions

@admin.register(CustomUser)
class UserAdminConfig(admin.ModelAdmin):
   search_field = ('email','username')
   ordering = ('-start_date',)
   list_filter = ('email', 'username', 'firstname', 'lastname','is_active', 'is_staff')
   list_display = ('email', 'username', 'firstname', 'lastname','is_active')
   fieldsets = (
       (None, {
           "fields": (
               'email', 'username', 'firstname', 'lastname', 
           ),
       }),
       ('permissions', {
         "fields": ('is_staff','is_active')
       }),
   )
   add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(Profile)
admin.site.register(Conditions)