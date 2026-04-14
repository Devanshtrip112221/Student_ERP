from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    return render(request,'index.html')


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error = "Invalid credentials or not authorized."

    return render(request,'admin_login.html',locals())
# Create your views here.


def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_dashboard')
    
    return render(request,'admin_dashboard.html')


def admin_logout(request):
    logout(request)
    return redirect('admin-login')

@login_required

def create_class(request):
    if request.method == 'POST':
        try:
            class_name = request.POST.get('classname')
            class_numeric = request.POST.get('classnamenumeric')
            section = request.POST.get('section')
            Class.objects.create(class_name=class_name,class_numeric=class_numeric,section=section)
            messages.success(request,"Class Created Successfully")
            return redirect('create_class')
        except Exception as e:
            messages.error(request,f"Something went wrong: {str(e)}")
            return redirect('create_class')
    return render(request,'create_class.html')

@login_required
def manage_classes(request):
    classes = Class.objects.all()

    

    if request.GET.get('delete'):
        try:
            class_id = request.GET.get('delete')
            class_obj = get_object_or_404(Class, id=class_id)
            class_obj.delete()

        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('manage_classes')

    return render(request,"manage_classes.html",locals()) 





@login_required

def edit_class(request,class_id):
        class_obj = get_object_or_404(Class, id=class_id)
        if request.method == 'POST':
            try:
                class_name = request.POST.get('classname')
                class_numeric = request.POST.get('classnamenumeric')
                section = request.POST.get('section')
                class_obj.class_name = class_name
                class_obj.class_numeric = class_numeric
                class_obj.section = section
                class_obj.save()

                messages.success(request,"Class Updated Successfully")
                return redirect('manage_classes')
            except Exception as e:
                messages.error(request,f"Something went wrong: {str(e)}")
                return redirect('edit_class')
        return render(request,"edit_class.html",locals()) 


@login_required
def create_subject(request):
    if request.method == 'POST':
        try:
            subject_name = request.POST.get('subjectname')
            subject_code = request.POST.get('subjectcode')
            
            Subject.objects.create(
                subject_name=subject_name,
                subject_code=subject_code
            )
            messages.success(request,"Subject Created Successfully")
            
        except Exception as e:
            messages.error(request,f"Something went wrong: {str(e)}")
        return redirect('create_subject')
    return render(request,'create_subject.html')


@login_required
def manage_subject(request):
    subjects = Subject.objects.all()

    

    if request.GET.get('delete'):
        try:
            subject_id = request.GET.get('delete')
            subject_obj = get_object_or_404(Subject, id=subject_id)
            subject_obj.delete()

        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('manage_subject')

    return render(request,"manage_subject.html",locals()) 

@login_required

def edit_subject(request,subject_id ):
        subject_obj  = get_object_or_404(Subject, id=subject_id )
        if request.method == 'POST':
            try:
                subject_name = request.POST.get('subjectname')
                subject_code = request.POST.get('subjectcode')
                
                subject_obj.subject_name = subject_name
                subject_obj.subject_code = subject_code
                
                subject_obj.save()

                messages.success(request,"subject Updated Successfully")
                
            except Exception as e:
                messages.error(request,f"Something went wrong: {str(e)}")
                return redirect('manage_subject')
        return render(request,"edit_subject.html",locals()) 




@login_required
def add_subject_combination(request):
    classes = Class.objects.all()
    subject = Subject.objects.all()

    if request.method == 'POST':
        try:
            class_id = request.POST.get('class')
            subject_id = request.POST.get('subject')
            
            SubjectCombination.objects.create(
                student_class=class_id,
                subject=subject_id,
                status = 1
            )
            messages.success(request,"Added Successfully")
            
        except Exception as e:
            messages.error(request,f"Something went wrong: {str(e)}")
        return redirect('add_subject_combination')
    return render(request,'add_subject_combination.html', locals())