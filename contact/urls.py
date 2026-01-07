from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact_views.contact, name='contact'),
    path('search', views.contact_views.search, name='search'),
    path('', views.contact_views.index, name='index'),
]
