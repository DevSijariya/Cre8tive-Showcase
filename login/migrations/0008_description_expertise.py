# Generated by Django 4.2.9 on 2024-02-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_project_description_alter_project_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutuser', models.TextField(max_length=500)),
                ('smalldescription', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feild_of_expertise', models.CharField(max_length=20)),
            ],
        ),
    ]
