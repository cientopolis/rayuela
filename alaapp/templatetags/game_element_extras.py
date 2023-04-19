from django import template
register = template.Library()

@register.simple_tag
def get_progress_user(ge,user_id):
    return float("%.2f" % ge.get_progress_user(user_id))

@register.simple_tag
def is_valued(ge,user_id):
    return ge.is_valued(user_id)

@register.simple_tag
def get_assignment_id(ge,user_id):
    return ge.get_assignment_id(user_id)

@register.simple_tag
def scoried(ge,user_id):
    return ge.scoried(user_id)

@register.simple_tag
def can_add(badge,user_id):
    return badge.can_add(user_id)