from django import forms
from django.db.models.base import Model
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
     "placeholder" : "Your description",   
    "class": "new-class-name two","id": 
    "my_id_for_textarea","rows": 20,"cols":120}))
    price = forms.DecimalField(initial=199.99)
    email = forms.EmailField()
    class Meta: 
        model = Product
        fields = [ 
            'title',
            'description',
            'price',
        ]
 
def clean_email(self,*args,**kwargs): 
    email = self.cleaned_data.get("email")
    if not email.endswith("edu"):
        raise forms.ValidationError("Not a valid Mail")
    return email

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
     "placeholder" : "Your description",   
    "class": "new-class-name two","id": 
    "my_id_for_textarea","rows": 20,"cols":120}))
    price = forms.DecimalField(initial=199.99)