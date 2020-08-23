from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('create/', views.create, name='create_student'),
    path('update_student/<str:pk>/', views.updateStudent, name='update_student'),
    path('list/', views.list, name='list'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student'),

]