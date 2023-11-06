from django.urls import path
from coursesApi import views

urlpatterns = [
    path("", views.home, name="home")
]
