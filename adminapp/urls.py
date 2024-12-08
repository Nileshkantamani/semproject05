from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.projecthomepage, name= 'projecthomepage'),
    path('UserLoginPageCall',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic',views.UserLoginLogic,name='UserLoginLogic'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('logout/',views.logout,name='logout'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_list/',views.EmployeeList ,name='employee_list'),
    #path('add_studentcall/', views.add_studentcall, name='add_studentcall'),
    #path('student_listcall/', views.student_listcall, name='student_listcall')
    path('feedback/', views.feedback_view, name='feedback'),
    path('add/', views.add_contact, name='add_contact'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),


]
