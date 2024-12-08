from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, AddCourse, EmployeeList
from .forms import TaskForm, MarksForm, AddCourseForm


def TrainerHomePage(request):
    return render(request, 'trainerapp/TrainerHomePage.html')


def add_blog(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainerapp:add_blog')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'trainerapp/add_blog.html', {'form': form, 'tasks': tasks})


def delete_blog(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('trainerapp:add_blog')


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainerapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'trainerapp/add_course.html', {'form': form})


def view_student_list(request):
    course = request.GET.get('course', '')
    section = request.GET.get('section', '')

    # Filter AddCourse based on course and section
    filtered_courses = AddCourse.objects.all()
    if course:
        filtered_courses = filtered_courses.filter(course=course)
    if section:
        filtered_courses = filtered_courses.filter(section=section)

    # Get employees related to the filtered courses
    employees = EmployeeList.objects.filter(id__in=filtered_courses.values('employee_id'))

    # Get dropdown choices from AddCourse model
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES

    context = {
        'employees': employees,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'trainerapp/view_employee_list.html', context)


def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the employee in the form
            employee = marks_instance.employee
            user_email = employee.user.email

            subject = 'Marks Entered'
            message = f'Hello, {employee.user.first_name}, marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'your_email@example.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'trainerapp/post_marks.html', {'form': form, 'success': True})
    else:
        form = MarksForm()
    return render(request, 'trainerapp/post_marks.html', {'form': form})



from django.shortcuts import render
from .models import AddCourse

def course_list_view(request):
    courses = AddCourse.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'ProjectHomePage.html', context)
