from django.contrib import admin
from rayuelaApp.models.role import Role
from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.scoring import Scoring
from rayuelaApp.models.criteria import Criteria
from rayuelaApp.models.day import Day
from rayuelaApp.models.token import Token
from rayuelaApp.models.check_in import CheckIn
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.time_restriction import TimeRestriction
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
