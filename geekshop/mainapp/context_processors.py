from basketapp.models import Basket


def basket(request):
    print('Привет, это контекстный процессор')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return {
        'basket': basket,
    }
