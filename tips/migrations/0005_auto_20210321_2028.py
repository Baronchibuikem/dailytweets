# Generated by Django 3.1.7 on 2021-03-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0004_auto_20210321_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytip',
            name='python_tip',
            field=models.TextField(max_length=500),
        ),
    ]