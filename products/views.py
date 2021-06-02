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

# def test_context(request):
#     with open('products/fixtures/goods_my.json', 'r', encoding='utf-8') as f_obj:
#         data = json.load(f_obj)
#
#     print(data)
#     print(type(data))
#     context = {
#         'title': 'G-Shop',
#         'header': 'Добро пожаловать',
#         'username': 'Сидор Сидоров',
#         'products': data,
#         #     [
#         #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
#         #     {'name': 'Синяя куртка The North Face', 'price': 23725},
#         #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
#         # ]
#     }
#     return render(request, 'products/test-context.html', context)
