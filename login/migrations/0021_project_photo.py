# Generated by Django 4.2.9 on 2024-02-29 15:28

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_templatechoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path),
        ),
    ]
