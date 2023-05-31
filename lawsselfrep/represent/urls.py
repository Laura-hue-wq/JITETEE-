from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.home, name='contact'),
    path('ai/', views.ai, name='ai'),
    path('error-handler/', views.error_handler, name='error_handler'),
]
