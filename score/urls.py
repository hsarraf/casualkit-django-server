from django.urls import include, path
from . import views


urlpatterns = [
    path(r'update/', views.update, name='update'),
]
