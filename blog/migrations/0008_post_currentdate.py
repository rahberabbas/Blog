# Generated by Django 2.2.7 on 2020-08-05 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200803_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='currentdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
