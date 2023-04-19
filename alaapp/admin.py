from django.contrib import admin
from alaapp.models.role import Role
from alaapp.models.user import User
from alaapp.models.project import Project
from alaapp.models.badge import Badge
from alaapp.models.scoring import Scoring
from alaapp.models.criteria import Criteria
from alaapp.models.day import Day
from alaapp.models.token import Token
from alaapp.models.check_in import CheckIn
from alaapp.models.project_subarea import ProjectSubArea
from alaapp.models.time_restriction import TimeRestriction
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','complete_name','username','email','password','profile_image','verified','role_id')
    readonly_fields= ('id',)

class RoleAdmin(admin.ModelAdmin):
    list_display=('id','name')

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','name','description','image')
    
class TokenAdmin(admin.ModelAdmin):
    list_display=('user_id','token')

class BadgeAdmin(admin.ModelAdmin):
    list_display=('image','parent')

class AreaAdmin(admin.ModelAdmin):
    list_display=('lat','long')

class CheckInAdmin(admin.ModelAdmin):
    list_display=('user','project','latitude','longitude','datetime')

class BadgeProgressAdmin(admin.ModelAdmin):
    list_display=('user','badge','progress')

class SubAreaAdmin(admin.ModelAdmin):
    list_display=('area','sub_area')

class CriteriaAdmin(admin.ModelAdmin):
    list_display=('id','name')

class ScoringAdmin(admin.ModelAdmin):
    list_display=('criteria','assignment','assessment')

class DayAdmin(admin.ModelAdmin):
    list_display= ('id','name')

class TimeRestrictionAdmin(admin.ModelAdmin):
    list_display= ('id','name','date_from','date_to','hour_from','hour_to')

admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Badge,BadgeAdmin)
admin.site.register(CheckIn,CheckInAdmin)
admin.site.register(ProjectSubArea,SubAreaAdmin)
admin.site.register(Scoring,ScoringAdmin)
admin.site.register(Criteria,CriteriaAdmin)
admin.site.register(Day,DayAdmin)
