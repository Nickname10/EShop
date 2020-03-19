from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from shop.models import Item, Order
from .cart import Cart


def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(item=item, update_quantity=True)
    print(cart.__dict__)
    return JsonResponse(
        {'Items': list(Item.objects.filter(id__in=map(int, cart.cart.keys())).values('id', 'title', 'price', 'image')),
         "Price": str(cart.get_total_price())})


def cart_view(request):
    cart = Cart(request)
    return JsonResponse(
        {'Items': list(Item.objects.filter(id__in=map(int, cart.cart.keys())).values('id', 'title', 'price', 'image')),
         "Price": str(cart.get_total_price())})


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return JsonResponse(
        {'Items': list(Item.objects.filter(id__in=map(int, cart.cart.keys())).values('id', 'title', 'price', 'image')),
         "Price": str(cart.get_total_price())})


def cart_buy(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        ordered_items = Item.objects.filter(id__in=map(int, cart.cart.keys())).all()
        for i in ordered_items:
            order = Order(profile=request.user.profile, item=i)
            order.save()
        cart.clear()
        return JsonResponse({"response": "OK"})
    else:
        return JsonResponse({"response": "REDIRECT"})
