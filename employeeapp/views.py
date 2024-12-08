from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from trainerapp.models import Marks, AddCourse
from adminapp.models import EmployeeList
from .models import Subheading, Topic, Certificate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def EmployeeHomePage(request):
    return render(request, 'employeeapp/EmployeeHomePage.html')

@login_required
def view_marks(request):
    user = request.user

    try:
        employee_user = User.objects.get(username=user.username)
        employee = EmployeeList.objects.get(user=employee_user)
        marks = Marks.objects.filter(employee=employee)

        return render(request, 'employeeapp/view_marks.html', {'marks': marks})
    except (EmployeeList.DoesNotExist, User.DoesNotExist):
        return render(request, 'employeeapp/no_employeelist.html', {
            'error': 'No student record found for this user.'
        })

@login_required
def employee_course(request):
    user = request.user

    try:
        employee_user = User.objects.get(username=user.username)
        employee = EmployeeList.objects.get(user=employee_user)
        courses = AddCourse.objects.filter(employee=employee)

        return render(request, 'employeeapp/employee_course.html', {'courses': courses})
    except (EmployeeList.DoesNotExist, User.DoesNotExist):
        return render(request, 'employeeapp/no_employeelist.html', {
            'error': 'No student record found for this user.'
        })


@login_required
def complete_course(request, course_id):
    if request.method == 'POST':  # Only handle POST request when the button is clicked
        user = request.user

        try:
            employee_user = User.objects.get(username=user.username)
            employee = EmployeeList.objects.get(user=employee_user)
            course = AddCourse.objects.get(id=course_id, employee=employee)

            # Check if the course is already completed
            if not Certificate.objects.filter(course=course, employee=employee).exists():
                Certificate.objects.create(course=course, employee=employee)

            # Redirect back to the course list after completing
            return redirect('employeeapp:employee_course')  # Change this to your actual URL name
        except (EmployeeList.DoesNotExist, User.DoesNotExist, AddCourse.DoesNotExist):
            return render(request, 'employeeapp/no_employeelist.html', {
                'error': 'No student record found for this user or invalid course.'
            })

    # Handle GET request or other scenarios
    return redirect('employeeapp:employee_course')
@login_required
def download_certificate(request, certificate_id):
    user = request.user

    try:
        employee_user = User.objects.get(username=user.username)
        employee = EmployeeList.objects.get(user=employee_user)
        certificate = Certificate.objects.get(id=certificate_id, employee=employee)
        response = HttpResponse(certificate.file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{certificate.course.name}_Certificate.pdf"'
        return response
    except (EmployeeList.DoesNotExist, User.DoesNotExist, Certificate.DoesNotExist):
        return render(request, 'employeeapp/no_employeelist.html', {
            'error': 'No student record found for this user or invalid certificate.'
        })
