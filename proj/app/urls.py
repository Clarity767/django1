from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/<int:job_id>/', views.detail, name='detail'),
]