from django.contrib import admin

from .models import Item, Comment, Category, SizeAndAvailable, Profile, WishItem, Order

# Register your models here.
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(SizeAndAvailable)
admin.site.register(Profile)
admin.site.register(WishItem)
admin.site.register(Order)
