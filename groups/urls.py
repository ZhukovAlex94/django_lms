from django.urls import path

from .views import (create_group, delete_group, detail_group)
from .views import UpdateGroupView
from .views import ListGroupView

app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', create_group, name='create'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
