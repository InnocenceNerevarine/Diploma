# Generated by Django 3.1.7 on 2021-05-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0021_auto_20210517_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категврии'),
        ),
    ]
