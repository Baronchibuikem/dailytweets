# Generated by Django 3.1.7 on 2021-03-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostDailyTip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('python_tip', models.CharField(max_length=140)),
                ('your_twitter_name', models.CharField(max_length=140)),
                ('your_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TweetLinks',
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tip_id', models.IntegerField()),
                ('python_tip', models.TextField(max_length=500)),
                ('posted_by', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateField()),
                ('likes', models.IntegerField()),
                ('retweets', models.IntegerField()),
                ('urls', models.ManyToManyField(to='tips.TweetLinks')),
            ],
            options={
                'ordering': ['-likes'],
            },
        ),
    ]