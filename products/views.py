from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

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
