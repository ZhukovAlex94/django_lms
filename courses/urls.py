from django.urls import path

from .views import CreateCourseView
from .views import DeleteCourseView
from .views import DetailCourseView
from .views import UpdateCourseView
from .views import get_courses


app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
]
