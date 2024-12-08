from django import forms
from .models import EmployeeList

class EmployeeListForm(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = ['register_number', 'full_name']
