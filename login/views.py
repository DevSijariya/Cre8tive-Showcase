from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout    
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UserProfileForm
from .forms import *
from django.shortcuts import get_object_or_404
import random
import string
from datetime import datetime, timedelta

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            return HttpResponse('Passwords are not matched')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')

    return render(request, 'login.html')


    

def home(request):
    return render(request, 'home.html')
def logoutpage(request):
    logout(request)
    return redirect('home')

def firstpage(request):
    return render(request, 'first.html')

@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES ,instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.save()
            return redirect('firstdetails')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'first.html', {'form': form})


def contact(request):
    user = request.user
    details = UserProfile.objects.get(user=user)
    if request.method == 'GET':
            form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
        # Retrieve form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            user_mail = 'sanskarsija59@gmail.com'

            context = {
                'subject': subject,
                'message': message,
                'sender_name': name,
                'sender_email': email,
            }
            html_content = render_to_string('email_template.html', context)
            plain_text_content = strip_tags(html_content)
            html_message = html_content
            send_mail(subject, plain_text_content, email, [user_mail], html_message=html_message, fail_silently=True)        

            # Optionally, you can redirect to a success page after sending the email
            return render(request, 'contact.html')
    context={
            'form':form,
            'details':details,
    }
    return render(request, 'contact.html',context)

@login_required
def details(request):
    details = UserProfile.objects.get(user=request.user)
    context = {'details': details}
    return render(request, 'firstdetail.html', context)


EducationFormSet = inlineformset_factory(User, Educationsdetail, form=EducationForm, extra=1)
@login_required
def add_education(request):
    formset = EducationFormSet(request.POST or None, queryset=Educationsdetail.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('education_details')
        else:
            print(formset.errors) 


    return render(request, 'second.html', {'formset': formset})


@login_required
def display_edu(request):
    user = request.user
    education_details = user.educationsdetail_set.all()
    details = UserProfile.objects.get(user=request.user)
    context = {
        'details': details,
        'user': user,
        'education_details': education_details,
    }
    return render(request, 'second_detail.html', context)

def delete_entry(request, education_id):
    education = get_object_or_404(Educationsdetail, id=education_id)
    
    if request.method == 'POST':
        education.delete()
        return redirect('education_details')
    
    
def add_skills(request):
    formset=skillformset(request.POST or None, queryset=skills.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('display_skills')
        else:
            print(formset.errors)
    return render(request, 'add_skill.html', {'formset': formset})

def display_skills(request):
    user=request.user
    skills_details=user.skills_details.all()
    details=UserProfile.objects.get(user=request.user)
    context={
        'details':details,
        'user':user,
        'skills_details':skills_details,
    }
    return render(request,'display_skills.html',context)

def delete_skill(request, skill_id):
    skill = get_object_or_404(skills, id=skill_id)
    
    if request.method == 'POST':
        skill.delete()
        return redirect('display_skills')
    

def add_projects(request):
    formset=projectformset(request.POST or None, queryset=Project.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('display_projects')
        else:
            print(formset.errors)
    return render(request, 'project.html', {'formset': formset})
def display_projects(request):
    user=request.user
    project_details=user.project_details.all()
    details=UserProfile.objects.get(user=request.user)
    context={
        'details':details,
        'user':user,
        'project_details':project_details,
    }
    return render(request, 'display_project.html',context)
def delete_project(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('display_projects')
    



def link(request):
    if request.method == 'POST':
        form=linkset(request.POST)
        if form.is_valid():
            user_profile = get_object_or_404(UserProfile, user=request.user)
            user_profile.links.all().delete()
            form.instance.user=user_profile
            form.save()
            return redirect('add_skills')
    else:
        form=linkset()
    return render(request, 'links.html',{'form':form})
def service(request):
    formset = ServicesFormSet(request.POST or None, queryset=services.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user 
                instance.save()
            return redirect('display_services')
        else:
            print(formset.errors)
    return render(request, 'add_services.html', {'formset': formset})
def display_services(request):
    user=request.user
    details=UserProfile.objects.get(user=request.user)
    service_details = details.user.service_details.all()
    context={
        'details':details,
        'user':user,
        'service_details':service_details,
    }
    return render(request, 'display_services.html',context)

from django.http import JsonResponse    
@login_required
def choose_template(request):
    if request.method == 'POST':
        template_choice = request.POST.get('template_choice')
        color_choice = request.POST.get('color_choice')
        user = request.user

        if template_choice:
            TemplateChoice.objects.update_or_create(user=user, defaults={'template_choice': template_choice, 'color_choice': color_choice})
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'error': 'Template choice is missing'}, status=400)
    return render(request, 'templates.html')


from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request, username):
    details = get_object_or_404(UserProfile, user__username=username)
    service_details = details.user.service_details.all()
    template_choice = TemplateChoice.objects.filter(user=details.user).first()
    project_details = details.user.project_details.all()
    skills_details = skills.objects.filter(user=details.user)
    education_details = Educationsdetail.objects.filter(user=details.user)
    linkdetail = links.objects.filter(user=details)
    
    context = {
        'details': details,
        'user': details.user,
        'education_details': education_details,
        'skills_details': skills_details,
        'link': linkdetail,
        'project_details': project_details,
        'template_choice': template_choice,
        'services': service_details,
        'user_name': username,
    }

    # Render template
    template_path = 'resume.html'
    template = get_template(template_path)
    html = template.render(context)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}_resume.pdf"'.format(username)

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation error!')

    return response


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
    
def portfolio(request, username):
    user = get_object_or_404(User, username=username)
    
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        # Increment portfolio views
        if request.user != user:
            user_profile.portfolio_views += 1
            user_profile.save()


        details = UserProfile.objects.get(user=user)
        service_details=user.service_details.all()
        template_choice = TemplateChoice.objects.filter(user=user).first()
        project_details=user.project_details.all()
        skills_details = skills.objects.filter(user=user)
        education_details = Educationsdetail.objects.filter(user=user)
       
        linkdetail=links.objects.filter(user=details)

        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                user_mail = details.email

                context = {
                    'subject': subject,
                    'message': message,
                    'sender_name': name,
                    'sender_email': email,
                }
                html_content = render_to_string('email_template.html', context)
                plain_text_content = strip_tags(html_content)
                html_message = html_content
                send_mail(subject, plain_text_content, email, [user_mail], html_message=html_message, fail_silently=True)        

        context = {
            'details': details,
            'user': user,
            'education_details': education_details,
            'skills_details': skills_details,
            'link':linkdetail,
            'project_details':project_details,
            'template_choice': template_choice,
            'form':form,
            'services':service_details,
            'portfolio_views': user_profile.portfolio_views if request.user == user else None,
        }

        return render(request, 'portfolio.html', context)
    except UserProfile.DoesNotExist:
        return HttpResponse("Please fill the details first.")

