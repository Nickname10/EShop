import hashlib
from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView

from .models import Item, Comment, WishItem

APP_URL = '/shop/'


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = APP_URL

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = APP_URL + 'login/'
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        form.save()
        form.data.get('')
        return super(RegisterFormView, self).form_valid(form)


def PasswordChangeView(request, hash):
    for us in User.objects.filter():
        if us.email:
            print(hashlib.sha1(str(us.email).encode('utf-8')).hexdigest())

            if hashlib.sha1(str(us.email).encode('utf-8')).hexdigest() == hash:
                print("hello world")
                password = User.objects.make_random_password()
                us.set_password(password)
                us.save()
                send_mail('Your new password: ', f'{password}',
                          'postManDjango228@gmail.com', [us.email], False)

                break
    return redirect(APP_URL)


class LogoutClickView(LogoutView):
    next_page = APP_URL


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html",
                      context={"Items": Item.objects.all()[0:9],
                               "User": request.user,
                               })

    def post(self, request, *args, **kwargs):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class WishListView(View):
    def get(self, request, *args, **kwargs):
        wish_item = WishItem()
        if request.user.is_authenticated:
            wish_item.item = get_object_or_404(Item, pk=kwargs['item_id'])
            wish_item.profile = request.user.profile
            wish_item.save()
            return JsonResponse({"Status": "OK"})
        else:
            return JsonResponse({"Status": "REDIRECT"})

    def post(self, request, *args, **kwargs):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class ItemsView(View):
    def get(self, request, *args, **kwargs):
        # time.sleep(2)

        min_price = request.GET.get('Min-value')[5:7] if len(request.GET.get('Min-value')) == 8 else request.GET.get(
            'Min-value')[5:8]
        max_price = request.GET.get('Max-value')[5:7] if len(request.GET.get('Max-value')) == 8 else request.GET.get(
            'Max-value')[5:8]
        result_response = Item.objects.all()
        result_response = result_response.filter(price__lt=max_price, price__gt=min_price)
        if request.GET.get("New") == "true":
            result_response = result_response.filter(isNewCollection=True)
        if request.GET.get("Discount") == "true":
            result_response = result_response.filter(discount_price=not None)
        if request.GET.getlist("Brand")[0] != '':
            result_response = result_response.filter(Brand__in=request.GET.getlist("Brand"))
        if request.GET.getlist("Sizes")[0] != '':
            result_response = result_response.filter(sizeandavailable__foot_size__in=request.GET.getlist("Sizes"))
        page = int(request.GET.get("Page"))
        result_comments = list(Comment.objects.filter(item__in=result_response).values('profile__photo',
                                                                                       'profile__user__username',
                                                                                       'date',
                                                                                       'text', 'item_id'))
        result_response = list(result_response.values('id', 'title', 'image',
                                                      'Brand', 'short_description',
                                                      'long_description', 'price')[page * 9:(page + 1) * 9])
        print(result_response)
        return JsonResponse({'Items': result_response,
                             'Comments': result_comments})

    def post(self, request, *args, **kwargs):
        HttpResponseNotFound('<h1>Page not found</h1>')


def search(request):
    result_response = Item.objects.all().filter(Q(title__contains=request.GET.get('str')))
    print(result_response)
    result_comments = list(Comment.objects.filter(item__in=result_response).values('profile__photo',
                                                                                   'profile__user__username',
                                                                                   'date',
                                                                                   'text', 'item_id'))
    result_response = list(result_response.values('id', 'title', 'image',
                                                  'Brand', 'short_description',
                                                  'long_description', 'price'))
    return JsonResponse({'Items': result_response, 'Comments': result_comments})


def addComment(request, item_id):
    if request.user.is_authenticated:
        comment = Comment()
        comment.profile = request.user.profile
        comment.text = request.POST['comment']
        comment.item = Item.objects.filter(id=item_id)[0]
        comment.date = datetime.now()
        comment.save()
        return HttpResponseRedirect(APP_URL)
    else:
        HttpResponseRedirect(APP_URL + '/login/')

    return HttpResponseRedirect(APP_URL + f'item/{id}')


class ForgetPassword(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/forget.html')

    def post(self, request, *args, **kwargs):
        mail = request.POST.get('email')
        print(mail)
        hash = hashlib.sha1(str(mail).encode('utf-8')).hexdigest()
        send_mail('Восстановление пароля: ', f'Нажмите: http://127.0.0.1:8000/shop/changePassword/{hash}',
                  'postManDjango228@gmail.com', [mail], False)
        return redirect(APP_URL)
