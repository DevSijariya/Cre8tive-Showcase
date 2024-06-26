# Generated by Django 4.2.9 on 2024-01-25 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_rename_education_educationsdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educationsdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('year_of_passing', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Educationsdetails',
        ),
    ]
