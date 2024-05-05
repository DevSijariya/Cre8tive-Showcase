from django import forms
from .models import *
from django.forms import inlineformset_factory

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'address','mobile_number','email','photo','aboutuser','User_description','Resume']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Educationsdetail
        fields = ['university','college', 'degree', 'year_of_passing','Cgpa']

EducationFormSet = inlineformset_factory(User, Educationsdetail, form=EducationForm, extra=1,can_delete=False)

class skillset(forms.ModelForm):
    class Meta:
        model=skills
        fields = ['skills','level']
skillformset = inlineformset_factory(User, skills,form=skillset,extra=1)

class projectset(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title','description','start_date','end_date','link']
projectformset= inlineformset_factory(User,Project,form=projectset,extra=1)


class linkset(forms.ModelForm):
    class Meta:
        model=links
        fields=['github','linkdin','facebook','instagram']

class Serviceset(forms.ModelForm):
    class Meta:
        model = services
        fields = ['title', 'description', 'year_of_experience']

ServicesFormSet = inlineformset_factory(User, services, form=Serviceset, extra=1)

class TemplateChoiceForm(forms.ModelForm):
    class Meta:
        model = TemplateChoice
        fields = ['template_choice']

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    subject=forms.CharField(required=True, label='Your Subject')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)