# Generated by Django 3.1.3 on 2020-11-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
