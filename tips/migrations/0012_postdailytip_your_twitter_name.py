# Generated by Django 3.1.7 on 2021-03-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0011_postdailytip'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdailytip',
            name='your_twitter_name',
            field=models.CharField(default='admin2@gmail.com', max_length=140),
            preserve_default=False,
        ),
    ]
