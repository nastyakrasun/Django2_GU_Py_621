from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from adminapp.forms import ShopUserRegisterForm, ProductEditForm, ProductCategoryEditForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return ShopUser.objects.filter(is_delete=False)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/shopuser_form.html'
    success_url = reverse_lazy('admin_staff:users')


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    title = 'Пользователи/Редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserRegisterForm(instance=edit_user)

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    title = 'Пользователи/Удаление'

    user_to_delete = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_to_delete.is_delete = True
        user_to_delete.is_active = False
        user_to_delete.save()

        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'delete_form': user_to_delete,
    }

    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda user: user.is_superuser)
def categories(request):
    title = 'Админка/Категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'
    form_class = ProductCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/Создание'
        return context


@user_passes_test(lambda user: user.is_superuser)
def category_update(request, pk):
    title = 'Категория/Редактирование'
    edit_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    context = {'title': title,
               'form': edit_form,
               }

    return render(request, 'adminapp/category_create.html', context)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    context_object_name = 'category_to_delete'
    success_url = reverse_lazy('admin_staff:categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)

        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))

        context.update({'category': category})

        return context


@user_passes_test(lambda user: user.is_superuser)
def products(request, pk):
    title = 'Админка/Категории продуктов'

    if pk == 0:
        categories = ProductCategory.objects.filter(is_delete=False)

        context = {
            'title': title,
            'objects': categories,
        }

        return render(request, 'adminapp/categories.html', context)

    category = get_object_or_404(ProductCategory, pk=pk)
    products_category = Product.objects.filter(category__pk=pk)

    context = {
        'title': title,
        'category': category,
        'objects': products_category,
    }

    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, pk):
    title = 'Продукты/Создание'
    product_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products'), args=[pk])
    else:
        product_form = ProductEditForm(initial={'category': product_category})

    context = {
        'title': title,
        'product_update_form': product_form,
        'category': product_category
    }

    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_read(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = f'Продукты/{product.name}'

    context = {
        'title': title,
        'product_name': product,
    }

    return render(request, 'adminapp/product_read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = f'Продукты/{product.name}'

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()

            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[product_form.pk]))
    else:
        product_form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'product_update_form': product_form,
        'category': product.category
    }

    return render(request, 'adminapp/product_update.html', context)

@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, pk):
    title = 'Продукты/Удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_delete = True
        product.save()

        return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))

    context = {
        'title': title,
        'product_to_delete': product,
    }

    return render(request, 'adminapp/product_delete.html', context)
