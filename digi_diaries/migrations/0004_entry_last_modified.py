# Generated by Django 5.1.2 on 2025-01-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_diaries', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
