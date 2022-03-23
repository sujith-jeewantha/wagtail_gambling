from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.

class SubPage(Page):

    template = "subpage/sub_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    contant_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]