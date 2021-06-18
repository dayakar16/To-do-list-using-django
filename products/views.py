from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

# def productFormView(request,*args,**kwargs):
#         form =  RawProductForm()
#         if request.method == 'POST':
#            form = RawProductForm(request.POST, None)
#            if form.is_valid():
#                    print(form.cleaned_data)
#                    Product.objects.create(title='New One')
#            else: 
#                 print(form.errors)
#         content = {
#                 'form' : form
#         }
#         return render(request,"Product/product_create.html",content)



# def productFormView(request,*args,**kwargs):
#         form = ProductForm(request.POST or None)
#         if form.is_valid(): 
#           form.save()
#           form = ProductForm()
#         content = {
#                 'form' : form
#         }
#         return render(request,"Product/product_create.html",content)


def productFormView(request):
        intial_data = { 
                "title": "Awesome Title"
        }
        form = RawProductForm(request.POST or None, initial=intial_data)
        context = { 
                'form': form
        }
        return render(request, "Product/product_create.html", context)

def product_view(request,*args,**kwargs):
    obj = Product.objects.get(id=1)
    content = {
            "object" : obj,
    }
    return render(request,"products/product_detail.html",content)