from django.urls import path

from .views import (create_student, DetailStudentView, DeleteStudentView)

# from .views import CustomUpdateStudentView
from .views import UpdateStudentView
from .views import ListStudentView

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    # path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),
    # path('update/<int:student_id>/', update_student, name='update'),
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
]
