from django.urls import path

from .views import (create_student, delete_student, detail_student,
                    get_students, update_student)

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
