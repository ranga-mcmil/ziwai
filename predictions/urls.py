from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'predictions'
urlpatterns = [
   path('', views.search, name='search'),
   path('results/', views.results, name='results'),
]