# Generated by Django 3.1.7 on 2021-03-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0007_auto_20210323_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailytip',
            options={'ordering': ['-likes']},
        ),
        migrations.AddField(
            model_name='dailytip',
            name='tip_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailytip',
            name='likes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailytip',
            name='retweets',
            field=models.IntegerField(),
        ),
    ]