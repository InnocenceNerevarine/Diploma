# Generated by Django 3.1.7 on 2021-04-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_auto_20210410_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfeatures',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeaturesvalidators',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeaturesvalidators',
            name='feature',
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cartproduct',
            options={},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
