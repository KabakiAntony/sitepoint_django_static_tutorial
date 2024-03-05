from django.urls import path
from .import views

app_name = 'static_demo'

urlpatterns = [
    path('', views.index, name="index"),
]
