from django import template
from metashare.repository.views import get_all_logged_in_users
register = template.Library()

@register.inclusion_tag('logged_in_user_list.html')
def render_logged_in_user_list():
    return { 'users': get_all_logged_in_users() }
