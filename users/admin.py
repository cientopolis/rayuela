from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import RayuelaUser, Volunteer

class RayuelaUserAdmin(BaseUserAdmin):
    pass
    # model = RayuelaUser
    #list_display = ['username', 'first_name', 'last_name', 'is_staff', 'is_administrator']
    # search_fields = ('email', 'first_name', 'last_name')
    # ordering = ('email',)


class VolunteerAdmin(RayuelaUserAdmin):
    pass
    #list_display = ['username', 'first_name', 'last_name', 'is_staff', 'is_administrator']
    # search_fields = ('email', 'first_name', 'last_name')
    # ordering = ('email',)


admin.site.unregister(Group)
admin.site.register(RayuelaUser, RayuelaUserAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
