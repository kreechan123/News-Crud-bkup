# Generated by Django 3.0.3 on 2020-02-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimage',
            name='upload',
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
