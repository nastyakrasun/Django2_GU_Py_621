from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

# def index(request, pk=None):
    # if pk:
    #     print(f'PK -- {pk}')

    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'hELLO',
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def contact(request):
	return render(request, 'geekshop/contact.html')
