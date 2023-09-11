from django.urls import path
from primeira_aplicação import views

urlpatterns = [
    path("", views.index, name="Index")
]