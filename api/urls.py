from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="test"),
    path("post/", views.calculate, name="calc"),
]