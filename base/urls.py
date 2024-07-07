from django.urls import path 
from .views import TaskList, TaksDetail, TaskCreate


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaksDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]