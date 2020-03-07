from django.db import models


# Create your models here.
class Item(models.Model):
    title = models.CharField('Название', max_length=255)
    price = models.FloatField('Стоимость, руб.')
    discount_price = models.FloatField('Стоимость со скидкой, руб.', blank=True, null=True)
    short_description = models.TextField(blank=True)
    long_description = models.TextField('Описание товра', blank=True, null=True)
    image = models.ImageField('Картинка товара',upload_to="media/", null=True)

    def __str__(self):
        return self.title
