import imp
from re import template
from django.db import models
from django.shortcuts import render

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


class HomePage(Page):
    pass
    
    # templates = "home/home_page.html"
    # banner_title = models.CharField(max_length=100, blank=False, null=True)

    # search_fields = Page.search_fields + [
    #     # index.SearchField('banner_title'),
    # ]

    # content_panels = Page.content_panels + [
    #     FieldPanel('banner_title'),
    # ]

    # @route(r'^subpage/$')
    # def  the_sub_page(self, request, *args, **kwargs):
    #     context = self.get_context(request, *args, **kwargs)

    #     return render(request, "home/sub_page.html", context)
    #     pass
