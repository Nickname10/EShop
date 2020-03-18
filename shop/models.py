from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


FOOT_SIZES = [
    (i, f"{i}") for i in range(32, 48)
]

BRANDS = [
    ('AD', 'ADIDAS'),
    ('FI', 'FILA'),
    ('PU', 'PUMA'),
    ('NI', 'NIKE')
]

COUNTRIES = [
    ('BY', 'Belarus'),
    ('RU', 'Russia'),
    ('UA', 'Ukraine'),
    ('KZ', 'Kazakhstan')
]

ROLES = [
    ('MA', 'MANAGER'),
    ('DE', 'DELIVER'),
    ('US', 'USER')
]


class Item(models.Model):
    title = models.CharField('Название', max_length=255)
    price = models.DecimalField('Стоимость, руб.', max_digits=10, decimal_places=2)
    discount_price = models.FloatField('Стоимость со скидкой, руб.', blank=True, null=True, default=None)
    short_description = models.TextField(blank=True)
    long_description = models.TextField('Описание товра', blank=True, null=True)
    image = models.ImageField('Картинка товара', upload_to="media/", null=True)
    isNewCollection = models.BooleanField('Новая ли коллекция', default=False, null=True)
    Brand = models.CharField(max_length=2, choices=BRANDS, null=True)

    def __str__(self):
        return self.title


class SizeAndAvailable(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    available = models.IntegerField('count', default=1)
    foot_size = models.IntegerField('size', choices=FOOT_SIZES, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=2, choices=COUNTRIES, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True, default='users/default.png')
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField('role', max_length=2, choices=ROLES, default='US', null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=0)
    text = models.TextField('Комментарий')
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=0, related_name='comments')

    def __str__(self):
        return f'{self.profile.user_id} {self.date}'


class WishItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wishedItems', null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
