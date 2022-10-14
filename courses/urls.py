from django.urls import path

from .views import (create_course, delete_course, detail_course, get_courses,
                    update_course)

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course, name='create'),
    path('detail/<int:course_id>/', detail_course, name='detail'),
    path('update/<int:course_id>/', update_course, name='update'),
    path('delete/<int:course_id>/', delete_course, name='delete'),
]
