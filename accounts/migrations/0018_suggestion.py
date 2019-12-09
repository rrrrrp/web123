# Generated by Django 2.2.6 on 2019-12-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20191102_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default=None, max_length=4)),
                ('suggestion', models.CharField(default=None, max_length=100, unique=True)),
            ],
        ),
    ]
