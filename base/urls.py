from base import views
from django.urls import path
from .views import TaskList,TaskDetails,CreateTask,UpdateTask,DeleteTask,CustomLogin,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('',TaskList.as_view(),name="tasks"),
    path('task/<int:pk>',TaskDetails.as_view(),name="task"),
    path('create/',CreateTask.as_view(),name='create'),
    path('update/<int:pk>',UpdateTask.as_view(),name='update'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='delete'),
]