from pydoc import classname
from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.

class SubPage(Page):
    pass

    # template = "subpage/sub_page.html"

    # subtitle = models.CharField(max_length=100, null=True, blank=True)
    # short_description = models.CharField(max_length=250)
    # body = RichTextField(blank=True)

class ContentPage(Page):
    # date = models.DateField("Post date")
    short_description = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('short_description'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('body', classname="full"),
    ]

    # search_fields = Page.search_fields + [
    #     index.SearchField('subtitle'),
    #     index.SearchField('short_description'),
    #     index.SearchField('body'),
    # ]

    # content_panels = Page.content_panels + [
    #     FieldPanel('subtitle'),
    #     FieldPanel('short_description'),
    #     FieldPanel('body', classname="full"),
    # ]

