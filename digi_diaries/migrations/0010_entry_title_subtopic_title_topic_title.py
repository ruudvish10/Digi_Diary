# Generated by Django 5.1.2 on 2025-02-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_diaries', '0009_remove_entry_topic_subtopic_entry_sub_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='empty', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtopic',
            name='title',
            field=models.CharField(default='empty', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default='empty', max_length=200),
            preserve_default=False,
        ),
    ]
