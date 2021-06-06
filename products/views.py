from django.shortcuts import render
import json

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)

def products(request):
    with open('products/fixtures/goods_my.json', 'r', encoding='utf-8') as f_obj:
        data_from_json = json.load(f_obj)
    context = {
        'title': 'GeekShop - Каталог',
        'products': data_from_json,
    }
    return render(request, 'products/products.html', context)
