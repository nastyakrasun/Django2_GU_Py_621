# Generated by Django 3.2.3 on 2021-06-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210601_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': ('продукт',), 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': ('категория',), 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images', verbose_name='изображение товара'),
        ),
    ]
