from django.shortcuts import render
from app.models import * 
from django.db.models import FloatField,F
from django.db.models.functions import Coalesce
# Create your views here.

def list_view(request):
    context = {
        "products" : Product.objects.annotate(
            discount_prices = Coalesce ('discount_price',0,output_field=FloatField()),
            total_price = F('price')-F('discount_prices')
        ),
    }
    return render(request, 'list.html', context)

def detail_view(request,id):
    context = {
        "product": Product.objects.annotate(
            discount_prices = Coalesce ('discount_price',0,output_field=FloatField()),
            total_price = F('price')-F('discount_prices')
        ).get(id=id),
    }
    return render(request, 'detail.html' , context)
def create_view(request):
    context = {}
    return render(request, 'create.html', context)