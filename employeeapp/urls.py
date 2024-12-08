from django.urls import path
from . import views

app_name = 'employeeapp'

urlpatterns = [
    path('', views.EmployeeHomePage, name='EmployeeHomePage'),
    path('view_marks/', views.view_marks, name='view_marks'),
    path('employee_course/', views.employee_course, name='employee_course'),
    path('employee_course/', views.employee_course, name='employee_course'),
    path('complete_course/<int:course_id>/', views.complete_course, name='complete_course'),
    path('download_certificate/<int:certificate_id>/', views.download_certificate, name='download_certificate'),
]
