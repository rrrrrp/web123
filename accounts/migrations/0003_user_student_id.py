# Generated by Django 2.2.6 on 2019-10-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_baseinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(default='0000000000', max_length=10, unique=True),
        ),
    ]
