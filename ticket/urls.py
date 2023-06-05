from django.urls import include, path
from . import views

urlpatterns = [
    path(r'issue_ticket/', views.issue_ticket, name='issue_ticket'),
]
