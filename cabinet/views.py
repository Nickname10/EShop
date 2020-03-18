from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from shop.models import Profile, Item, Order
from .forms import UserForm, ItemForm


class UserCabinet(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            if request.user.profile.role == 'US':
                return render(request, 'user_cabinet.html', context={
                    "User": request.user,
                    "WishedItems": request.user.profile.wishedItems.all(),
                    "form": UserForm()
                })
            elif request.user.profile.role == 'MA':
                return render(request, 'manager_cabinet.html', context={
                    "User": request.user,
                    "Items": Item.objects.all(),
                    "form": ItemForm()
                })
            elif request.user.profile.role == 'DE':
                return render(request, 'deliver_cabinet.html', context={
                    "User": request.user,
                    "Order": Order.objects.all()
                })
        else:
            return redirect('/shop/login/')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = get_object_or_404(Profile, user=request.user)
            if request.user.profile.role == 'US':
                if request.FILES.get('photo'):
                    current_user.photo = request.FILES.get('photo')
                form = UserForm(request.POST)
                if form.is_valid():
                    if form.cleaned_data['phone_number'] != '':
                        current_user.phone_number = form.cleaned_data['phone_number']
                    if form.cleaned_data['email'] != '':
                        current_user.user.email = form.cleaned_data['email']
                    if form.cleaned_data['first_name'] != '':
                        current_user.user.first_name = form.cleaned_data['first_name']
                    if form.cleaned_data['last_name'] != '':
                        current_user.user.last_name = form.cleaned_data['last_name']
                    if form.cleaned_data['address'] != '':
                        current_user.address = form.cleaned_data['address']
                    current_user.user.save()
                    current_user.save()
                    return HttpResponseRedirect('/shop/cabinet/')
            elif request.user.profile.role == 'MA':
                item_form = ItemForm(request.POST)
                if item_form.is_valid():
                    item = Item(title=item_form.data.get('title'), Brand=item_form.data.get('Brand'),
                                short_description=item_form.data.get('short_description'),
                                long_description=item_form.data.get('long_description'),
                                price=item_form.data.get('price'),
                                isNewCollection=bool(item_form.data.get('isNewCollection')),
                                image=request.FILES.get('photo')
                                )
                    item.save()
                    return render(request, 'manager_cabinet.html', context={
                        "User": request.user,
                        "Items": Item.objects.all(),
                        "form": ItemForm()
                    })
                else:
                    return render(request, 'manager_cabinet.html', context={
                        "User": request.user,
                        "Items": Item.objects.all(),
                        "form": ItemForm()
                    })

        else:
            return redirect('/shop/login/')


class RemoveItemView(View):
    def post(self, request, item_id, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.role == 'MA':
            Item.objects.get(id=item_id).delete()
            return render(request, 'manager_cabinet.html', context={
                "User": request.user,
                "Items": Item.objects.all(),
                "form": ItemForm()
            })

        else:
            HttpResponseNotFound('<h1>Page not found</h1>')

    def get(self, request, item_id, *args, **kwargs):
        HttpResponseNotFound('<h1>Page not found</h1>')


class OrderDeliverView(View):
    def post(self, request, order_id, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.role == 'DE':
            Order.objects.get(id=order_id).delete()
            return render(request, 'deliver_cabinet.html', context={
                "User": request.user,
                "Order": Order.objects.all()
            })

    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class CreateItem(View):
    def post(self, request, *args, **kwargs):
        print("helo")
        item = Item(ItemForm(request.POST))
        item.save()
        return render(request, 'manager_cabinet.html', context={
            "User": request.user,
            "Items": Item.objects.all(),
            "form": ItemForm()
        })
