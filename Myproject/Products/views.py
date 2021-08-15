from django.shortcuts import render
from .models import Products
def products(request):
    prd=Products.objects.all()

    return render(request, 'product/product.html', {'msg':prd})
# Create your views here.
