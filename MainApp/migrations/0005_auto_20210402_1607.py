# Generated by Django 3.1.7 on 2021-04-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20210402_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_capacity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраиваемой памяти'),
        ),
    ]
