from django.urls import path
from . import views

app_name = 'trainerapp'

urlpatterns = [
    path('TrainerHomePage/', views.TrainerHomePage, name="TrainerHomePage"),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<int:pk>/delete_blog/', views.delete_blog, name='delete_blog'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('post_marks/', views.post_marks, name='post_marks'),
]
