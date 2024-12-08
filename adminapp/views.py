from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .models import Task, EmployeeList, Contact, Feedback
from .forms import TaskForm, EmployeeForm, ContactForm, FeedbackForm

# Create your views here.
def projecthomepage(request):
    return render(request, 'ProjectHomePage.html')

def UserLoginPageCall(request):
    return render(request, 'adminapp/loginpage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('employeeapp:EmployeeHomePage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('trainerapp:TrainerHomePage')
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')

def logout(request):
    auth_logout(request)
    return redirect('projecthomepage')

def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/ProjectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegisterPage.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                employee.user = user
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_employee.html', {'form': form})
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'adminapp/add_employee.html', {'form': form})

def add_employeecall(request):
    return render(request, 'adminapp/add_employee.html')

def employee_list(request):
    employees = EmployeeList.objects.all()
    return render(request, 'adminapp/employee_list.html', {'employees': employees})

def employee_listcall(request):
    return render(request, 'adminapp/employee_list.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'adminapp/confirmation.html')
    else:
        form = FeedbackForm()
    return render(request, 'adminapp/feedback_form.html', {'form': form})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            recipient_email = request.POST.get('recipient_email')
            if recipient_email:
                send_mail(
                    subject='New Contact Created',
                    message=f'Contact Details:\nName: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email]
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(models.Q(name__icontains=query) | models.Q(email__icontains=query))
    else:
        contacts = Contact.objects.all()
    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')
