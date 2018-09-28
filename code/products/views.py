from django.shortcuts import render
from .forms import RawProductForm
from .models import Product
# from .forms import RawProductForm
# Create your views here.


def product_create_view(request):
    context = {
        "form" : RawProductForm()
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     context : {}
#     return render(request, "products/product_create.html")



# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form':form
#     }
#     return render(request, "products/product_create.html",context)