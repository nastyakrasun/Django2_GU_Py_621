from django import forms

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import Product


class ShopUserRegisterForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'is_active', 'is_staff')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_txt = ''

class ProductEditForm(ShopUserEditForm):
    class Meta:
        model = Product
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_txt = ''


def ProductCategoryEditForm():
    return None