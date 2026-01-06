from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_views.index, name='index'),
]
