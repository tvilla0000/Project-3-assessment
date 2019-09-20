from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('widget/<int:wid_id>/', views.delete, name="delete"),
]