from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import inlineformset_factory
from django.dispatch import receiver
from django.db.models.signals import pre_delete,pre_save
from django.utils import timezone
import os
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_photo_size(value):
    filesize = value.size
    
    # Max size in bytes (5MB)
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")

def user_directory_path(UserProfile, filename):
    # Upload image to user's folder inside user_photos directory
    return f'user_photos/{UserProfile.user.username}/{timezone.now().strftime("%Y-%m-%d_%H-%M-%S")}_{filename}'

def user_pdf_upload_path(instance, filename):
    return 'pdf/{0}/{1}'.format(instance.user.username, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)    
    # Yahan aap apne user-specific details ko define kar sakte hain
    # Jaise ki:
 
    portfolio_views = models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),  # Allow only certain file extensions
           validate_photo_size,  # Maximum file size in bytes (e.g., 5 MB)
        ])
    aboutuser=models.CharField(max_length=200,default='Describe About Yourself in 2 Lines')
    User_description = models.TextField(max_length=1000,default='Describe Something About Yourself')
    Resume = models.FileField(upload_to=user_pdf_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the instance has been saved previously
        if self.pk:
            try:
                old_instance = UserProfile.objects.get(pk=self.pk)
                # Check if the old instance has a resume file and it exists
                if old_instance.Resume and os.path.exists(old_instance.Resume.path):
                    os.remove(old_instance.Resume.path)
            except UserProfile.DoesNotExist:
                pass

        super().save(*args, **kwargs)


class Educationsdetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university=models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year_of_passing = models.IntegerField()
    Cgpa=models.FloatField()

class skills(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='skills_details')
    skills=models.CharField(max_length=20)
    level=models.IntegerField()

def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='project_details')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=50,unique=True,null=True,blank=True)


class links(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='links')
    github=models.URLField(null=True,blank=True)
    linkdin=models.URLField(null=True,blank=True)
    facebook=models.URLField(unique=True,null=True,blank=True)
    instagram=models.URLField(unique=True,null=True,blank=True)

class services(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='service_details')
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    year_of_experience=models.IntegerField()

class work_experience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='work_details')
    post=models.CharField(max_length=100)
    join=models.IntegerField()
    end=models.IntegerField()
    desc=models.CharField(max_length=500)
    

class TemplateChoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    template_choice = models.CharField(max_length=10, choices=[
        ('1', 'Template 1'),
        ('2', 'Template 2'),
        ('3', 'Template 3'),
    ],default='1')
    color_choice = models.CharField(max_length=7)

    def __str__(self):
        return f"Template choice for {self.user.username}"


@receiver(pre_save, sender=UserProfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    # Delete old image file from storage when UserProfile object is updated
    if instance.pk:
        try:
            old_instance = UserProfile.objects.get(pk=instance.pk)
            if old_instance.photo and old_instance.photo != instance.photo:
                old_file_path = old_instance.photo.path
                if os.path.exists(old_file_path):
                    print(f"Deleting old file: {old_file_path}")
                    os.remove(old_file_path)
        except UserProfile.DoesNotExist:
            pass  # Old instance not found, nothing to delete

@receiver(pre_delete, sender=UserProfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    # Delete image file from storage before UserProfile object is deleted.
    if instance.photo:
        file_path = instance.photo.path
        if os.path.exists(file_path):
            print(f"Deleting file: {file_path}")
            os.remove(file_path)    
