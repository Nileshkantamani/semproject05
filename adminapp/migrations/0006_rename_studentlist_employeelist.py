# Generated by Django 5.1.3 on 2024-12-02 09:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_contact'),
        ('trainerapp', '0004_rename_student_addcourse_employee_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentList',
            new_name='EmployeeList',
        ),
    ]