# Generated by Django 4.2.9 on 2024-02-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_delete_link_delete_userlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(unique=True)),
                ('linkdin', models.URLField(unique=True)),
                ('facebook', models.URLField(blank=True, null=True, unique=True)),
                ('instagram', models.URLField(blank=True, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='login.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]