# Generated by Django 2.2.6 on 2019-10-13 14:27

import challenges.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('name', models.CharField(max_length=250, unique=True)),
                ('challenge_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('points', models.IntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to=challenges.models.get_upload_path)),
                ('flag', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengesSolvedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=250)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
