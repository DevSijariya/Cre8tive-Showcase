# Generated by Django 4.2.9 on 2024-03-02 04:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import login.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0024_alter_services_description_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_details', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), login.models.validate_photo_size]),
        ),
    ]
