# Generated by Django 2.2.7 on 2020-08-05 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_currentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ctime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
