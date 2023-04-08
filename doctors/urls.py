from django.urls import path
from . import views


app_name = 'doctors'
urlpatterns = [
   path('', views.doctors, name='doctors'),   
   path('<int:id>/', views.doctor, name='doctor'),
   path('delete/<int:id>/', views.delete, name='delete'),
   path('edit/<int:id>/', views.edit, name='edit'),
   path('new/', views.new, name='new'),   

]