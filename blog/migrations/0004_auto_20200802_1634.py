# Generated by Django 2.2.7 on 2020-08-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank='True', null='True', upload_to='images/'),
        ),
    ]
