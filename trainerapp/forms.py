from django import forms
from .models import Task, AddCourse, Marks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['employee', 'course', 'section']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['employee', 'course', 'marks']
