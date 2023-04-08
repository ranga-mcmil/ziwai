from django.urls import path
from . import views


app_name = 'patients'
urlpatterns = [
   path('', views.patients, name='patients'),   
   path('<int:id>/', views.patient, name='patient'),
   path('delete/<int:id>/', views.delete, name='delete'),
   path('edit/<int:id>/', views.edit, name='edit'),
   path('new/', views.new, name='new'),   
   path('prescriptions/', views.prescriptions, name='prescriptions'),   
   path('prescriptions/<int:id>/', views.prescription, name='prescription'),  
   path('prescriptions/new/', views.new_prescription, name='new_prescription'), 
]