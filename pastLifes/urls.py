from django.urls import path
from . import views

app_name = 'pastLifes'

urlpatterns = [
    path('', views.index, name='index'),
    path('showpast/', views.showpast, name='showpast'),
]
