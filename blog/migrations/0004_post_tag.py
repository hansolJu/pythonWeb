# Generated by Django 2.0.4 on 2018-04-09 00:35

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180409_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
