from django.urls import include, path
from . import views

urlpatterns = [
    path(r'verify/', views.verify, name='verify'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
]
