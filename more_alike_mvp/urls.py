from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='more-alike-home'),
    path('about/', views.about, name='more-alike-about'),

]
