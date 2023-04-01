from pyexpat import model
from django import forms
from django.forms import formset_factory
from .models import Invoice 

class InvoiceForm(forms.Form):
    # class Meta:
    model = Invoice
    fields = ['student_name','customer_email','billing_address','message']

    student_name = forms.CharField(
        label='Student_Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'student_name',
            'rows':1
        })
    )
    student_email = forms.CharField(
        label='Student Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'student_name@company.com',
            'rows':1
        })
    )
    mobile = forms.CharField(
        label='Mobile Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'mobile number',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    message = forms.CharField(
        label='Message/Note',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'message',
            'rows':1
        })
    )

class LineItemForm(forms.Form):
    # class Meta:
    model = Invoice
    fields = ['service','description','quantity','rate']

    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Book Name here',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)

class InvoiceUpdateform(forms.Form): 
        # class Meta:/
            model = Invoice 
            fields = ['student_name','customer_email','billing_address','message','service','description','quantity']
    