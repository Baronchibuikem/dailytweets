# Generated by Django 3.1.7 on 2021-03-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_auto_20210321_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytip',
            name='link',
        ),
        migrations.AddField(
            model_name='dailytip',
            name='display_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailytip',
            name='expanded_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailytip',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
