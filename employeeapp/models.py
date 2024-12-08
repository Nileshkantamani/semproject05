# employeeapp/models.py
from django.db import models
from django.contrib.auth.models import User

class EmployeeList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='employee_employee')

    def __str__(self):
        return self.Register_Number

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subheading(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Topic(models.Model):
    subheading = models.ForeignKey(Subheading, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Certificate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
