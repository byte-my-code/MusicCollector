from django import template

from website.base.models import gtm_manager

register = template.Library()

@register.simple_tag
def get_gtm_uid():
    instance = gtm_manager.objects.filter(live=True).first()
    uid = instance.uid if instance else "" 

    return uid