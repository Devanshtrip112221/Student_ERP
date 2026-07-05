"""
URL configuration for StudentResultManagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from resultapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name= 'index'),
    path("admin-login/",admin_login,name = "admin-login"),
    path("admin_dashboard/",admin_dashboard,name = "admin_dashboard"),
    path("create_class/",create_class,name="create_class"),
    path("admin_logout/",admin_logout,name="admin_logout"),
    path("manage_classes/",manage_classes,name="manage_classes"),
    path('edit_class/<int:class_id>/', edit_class, name='edit_class'),
    path("create_subject/",create_subject,name="create_subject"),
    path('manage_subject/',manage_subject,name="manage_subject"),
    path('edit_subject/<int:subject_id>/', edit_subject, name='edit_subject'),
    path('add_subject_combination/',add_subject_combination,name='add_subject_combination'),
    path('manage_subject_combination/',manage_subject_combination,name='manage_subject_combination'),
    path('create_student/', create_student, name='create_student'),
    path('manage_student/', manage_student, name='manage_student'),
    path('add_notice/', add_notice, name='add_notice'),
    path('manage_notice/', manage_notice, name='manage_notice'),
    path("add_result/", add_result, name="add_result"),
    path("get_student_subjects/",get_student_subjects,name='get_student_subjects'),
    path("manage_result/",manage_result,name="manage_result"),
    path("chage_password/",chage_password,name="chage_password"),
    path("search_result/",search_result,name="search_result"),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    # path("student_login/",student_login,name="student_login")
]
