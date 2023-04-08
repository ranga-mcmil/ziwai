from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
   path('', views.appointments, name='appointments'),   
   path('<int:id>/', views.appointment, name='appointment'),
   path('delete/<int:id>/', views.delete, name='delete'),
   path('edit/<int:id>/', views.edit, name='edit'),
   path('new/', views.new, name='new'),   

]