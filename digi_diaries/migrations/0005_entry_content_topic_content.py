# Generated by Django 5.1.2 on 2025-01-14 17:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digi_diaries', '0004_entry_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='empty'),
            preserve_default=False,
        ),
    ]
