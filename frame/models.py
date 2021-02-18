from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.api import APIField
from base.blocks import BaseStreamBlock
from base.history import HistoryStreamBlock

class FramePage(Page):
    prev = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='预览图',
        verbose_name="预览图"
    )
    
    top = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='框顶部',
        verbose_name="框顶部"
    )
    
    bottom = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='框底部',
        verbose_name="框底部"
    )
    
    content = StreamField(
        BaseStreamBlock(), verbose_name="介绍", blank=True
    )

    history = StreamField(
        HistoryStreamBlock(), verbose_name="历史效果图", blank=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('prev'),
        ImageChooserPanel('top'),
        ImageChooserPanel('bottom'),
        StreamFieldPanel ('content'),
        StreamFieldPanel ('history'),
    ]
    api_fields = [
        APIField('prev'),
        APIField('top'),
        APIField('bottom'),
        APIField('content'),
        APIField('history'),
    ]

class CardPage(Page):
    prev = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='预览图',
        verbose_name="预览图"
    )
    
    img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='图案',
        verbose_name="图案"
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('prev'),
        ImageChooserPanel('img'),
    ]

    api_fields = [
        APIField('prev'),
        APIField('img'),
    ]

class ScenePage(Page):
    prev = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='预览',
        verbose_name="预览"
    )
    
    img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='图案',
        verbose_name="图案"
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('prev'),
        ImageChooserPanel('img'),
    ]

    api_fields = [
        APIField('prev'),
        APIField('img'),
    ]
