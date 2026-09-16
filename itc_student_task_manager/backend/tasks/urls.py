from django.urls import path
from .views import RegisterView,LoginView,TaskListCreate,TaskDetail
urlpatterns=[path('register/',RegisterView.as_view()),path('login/',LoginView.as_view()),path('tasks/',TaskListCreate.as_view()),path('tasks/<int:pk>/',TaskDetail.as_view())]
