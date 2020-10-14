from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.api import APIField
from base.blocks import BaseStreamBlock

class FramePage(Page):
    prev = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='preview'
    )
    
    top = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='top of the frame'
    )
    
    bottom = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='bottom of the frame'
    )
    
    content = StreamField(
        BaseStreamBlock(), verbose_name="content", blank=True
    )


    content_panels = Page.content_panels + [
        ImageChooserPanel('prev'),
        ImageChooserPanel('top'),
        ImageChooserPanel('bottom'),
        StreamFieldPanel ('content'),
    ]
    api_fields = [
        APIField('prev'),
        APIField('top'),
        APIField('bottom'),
        APIField('content'),
    ]

class CardPage(Page):
    prev = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='preview'
    )
    
    img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='img'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('prev'),
        ImageChooserPanel('img'),
    ]

    api_fields = [
        APIField('prev'),
        APIField('img'),
    ]
