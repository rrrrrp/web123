# Generated by Django 2.2.6 on 2019-11-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_auto_20191029_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='scene',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
