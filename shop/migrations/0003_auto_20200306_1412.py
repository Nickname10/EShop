# Generated by Django 3.0.3 on 2020-03-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='shop/static/img/'),
        ),
    ]