from django.urls import path
from . import views


app_name = 'payments'
urlpatterns = [
    # Invoices
    path('invoices/new/', views.new_invoice, name='new_invoice'),
    path('invoices/<int:id>/', views.invoice, name='invoice'),
    path('invoices/', views.invoices, name='invoices'),

    
    # Payments
    path('', views.payments, name='payments'),   
    path('new/<int:id>/', views.new, name='new'),   
]