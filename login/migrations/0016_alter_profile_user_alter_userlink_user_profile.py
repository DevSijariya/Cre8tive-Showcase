# Generated by Django 4.2.9 on 2024-02-11 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_remove_userlink_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.userprofile'),
        ),
        migrations.AlterField(
            model_name='userlink',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.userprofile'),
        ),
    ]
