from django.urls import path
from . import views

app_name = 'menuai'

urlpatterns = [
    path('', views.home, name='home'),
    path('terms_of_service/', views.terms, name='terms_of_service'),
    path('contact/', views.contact, name='contact'),
]