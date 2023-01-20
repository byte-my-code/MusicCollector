from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import (
    DraftStateMixin,
    Page,
    PreviewableMixin,
    RevisionMixin,
)

from wagtail.snippets.models import register_snippet

# Google Tag Manager snippet
@register_snippet
class gtm_manager(DraftStateMixin, RevisionMixin, PreviewableMixin, models.Model):
    """
    Allows the site administrator to add their GTM to the site.
    Returns the first live tag set in the admin panel
    
    @TODO Constrain this to one instance only
    """
    uid = models.CharField(max_length=64, blank=True, null=True,
        help_text="Your unique code for GTM")
    
    panels = [
        FieldPanel('uid')
    ]

    def __str__(self):
        return self.uid
    
    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return { "gtm_uid" : self.uid }
    
    class Meta:
        verbose_name = "Google Tag Manager"
        verbose_name_plural = "Google Tag Manager"

class HomePage(Page):
    pass
