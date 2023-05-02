from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('update/<int:id>/', views.UpdateTask, name='Update'),
    path('delete/<int:id>/', views.DeleteTask, name='Delete'),
]
