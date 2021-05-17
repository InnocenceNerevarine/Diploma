# Generated by Django 3.1.7 on 2021-05-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0020_auto_20210419_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзину', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False, verbose_name='Анонимный пользователь'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False, verbose_name='В заказе'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='MainApp.CartProduct', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='session_key',
            field=models.CharField(max_length=100, null=True, verbose_name='Ключ сессии'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_products',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество товаров'),
        ),
    ]
