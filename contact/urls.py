from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    #contact views
    path('contact/<int:contact_id>/detail/', views.contact_views.contact, name='contact'),
    path('contact/create/', views.contact_forms.create, name='create'),
    path('contact/<int:contact_id>/update/', views.contact_forms.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.contact_forms.delete, name='delete'),
    
    #user views
    path('user/create/', views.user_forms.register, name='register'),
    
    
    #read views
    path('search', views.contact_views.search, name='search'),
    path('', views.contact_views.index, name='index'),
]
