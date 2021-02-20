# Generated by Django 3.1.6 on 2021-02-20 11:03

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0013_auto_20210220_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framepage',
            name='history',
            field=wagtail.core.fields.StreamField([('history', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(null=True, required=False)), ('card_page', wagtail.core.blocks.PageChooserBlock(null=True, required=False))]))], blank=True, null=True, verbose_name='历史效果图'),
        ),
    ]
