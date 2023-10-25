from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello),
    path('goodbye/', views.goodbye),
]