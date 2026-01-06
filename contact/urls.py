from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact_views.contact, name='contact'),
    path('', views.contact_views.index, name='index'),
]
