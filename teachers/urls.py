from django.urls import path

from .views import (create_teacher, delete_teacher, detail_teacher,
                    get_teachers, update_teacher)

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
