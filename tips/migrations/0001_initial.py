# Generated by Django 3.1.7 on 2021-03-21 18:13

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('expanded_url', models.URLField()),
                ('display_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyTip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python_tip', models.CharField(max_length=500)),
                ('posted_by', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=50)),
                ('timestamp', models.DateField()),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailytips', to='tips.link')),
            ],
            managers=[
                ('tweets', django.db.models.manager.Manager()),
            ],
        ),
    ]