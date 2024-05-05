"""
URL configuration for myport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




# from django.views.static import serve
from django.contrib import admin
from django.urls import path
from login import views
from django.contrib.auth import views as auth_view
from login.views import user_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('accounts/login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('logout/',views.logoutpage,name='logout'),
    path('Forgot/Password/',auth_view.PasswordResetView.as_view(),name='password_reset'),
    path('Password/reset/', auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('Password/reset/complete/sucessfully/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('user/details/', views.details, name='firstdetails'),
    path('user/profile/', user_profile, name='user_profile'),
    path('contact/admin/panel/', views.contact,name='contact'),
    path('Educationform/',views.add_education,name='add_education'),
    path('Education/details',views.display_edu,name='education_details'),
    path('delete_entry/<int:education_id>/', views.delete_entry, name='delete_entry'), 
    path('add/skills/',views.add_skills,name='add_skills'),
    path('display/skills/',views.display_skills,name='display_skills'), 
    path('delete/skills/<int:skill_id>/', views.delete_skill, name='delete_skill'), 
    path('add/projects/', views.add_projects, name='add_projects'),
    path('display/projects/',views.display_projects,name='display_projects'),
    path('delete/projects/<int:project_id>/', views.delete_project, name='delete_project'),
    path('add/users/links/',views.link,name='links'),
    path('add/users/services/',views.service,name='services'),
    path('display/users/services/',views.display_services,name='display_services'),
    path('add/users/templates/',views.choose_template,name='templates_page'),
    path('generate-pdf/<str:username>/', views.generate_pdf, name='generate_pdf'),
    path('user/<str:username>/portfolio/', views.portfolio, name='portfolio'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)