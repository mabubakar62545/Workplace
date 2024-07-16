from django.urls import path
from . import views

urlpatterns = [
    path('menu/<str:name>', views.menu),
]
