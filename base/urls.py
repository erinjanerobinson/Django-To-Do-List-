from django.urls import path 
from .views import TaskList, TaksDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaksDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]