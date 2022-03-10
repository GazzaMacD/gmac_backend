from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogPage(Page):
    # Fields
    read_length = models.PositiveSmallIntegerField(
        null=False, blank=False, help_text="Length of read in number of minutes"
    )

    # Panels
    content_panels = Page.content_panels + [
        FieldPanel("read_length"),
    ]
    # APi
    api_fields = [
        APIField("read_length"),
    ]
