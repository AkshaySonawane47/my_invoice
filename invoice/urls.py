from django.contrib import admin
from django.urls import path
from invoice import views
from .views import InvoiceListView 
# createInvoice, generate_PDF, view_PDF

app_name = 'invoice'
urlpatterns = [
    path('', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', views.createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', views.view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', views.generate_PDF, name='invoice-download'),
    path('update_invoice/<id>', views.update_invoice, name='update_invoice'),
    path('checkout', views.checkout, name='checkout.html'),
    
]
