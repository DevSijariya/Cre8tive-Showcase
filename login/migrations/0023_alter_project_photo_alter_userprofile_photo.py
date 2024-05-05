# Generated by Django 4.2.9 on 2024-02-29 15:49

import django.core.validators
from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), login.models.validate_photo_size]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), login.models.validate_photo_size]),
        ),
    ]