from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="test"),
    path("", views.calculate, name="calc"),
]