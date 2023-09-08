from django import template
register = template.Library()

@register.simple_tag
def is_my_admin(project,admin_id):
    return project.is_my_admin(admin_id)

@register.simple_tag
def is_my_time_restriction(project,time_restriction_id):
    return project.is_my_time_restriction(time_restriction_id)
