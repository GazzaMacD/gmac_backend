from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(HomePage, cls).can_create_at(parent) and not cls.objects.exists()
