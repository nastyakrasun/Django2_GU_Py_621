from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'some_name': 'Hello',
        'title': title,
        'slogan': 'супер-предложения',
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)
