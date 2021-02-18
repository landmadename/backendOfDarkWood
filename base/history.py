from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (StreamBlock, StructBlock, PageChooserBlock)


class History(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    card_page = PageChooserBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"

class HistoryStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    history = History()