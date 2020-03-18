import time
from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView

from .models import Item, Comment,WishItem

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
        return super(RegisterFormView, self).form_valid(form)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = APP_URL + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


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
        result_response = Item.objects.all()
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
        return JsonResponse({'Items': result_response,
                             'Comments': result_comments})

    def post(self, request, *args, **kwargs):
        HttpResponseNotFound('<h1>Page not found</h1>')


def addComment(request, id):
    comment = Comment()
    comment.user = request.user
    comment.text = request.POST['message']
    comment.item = get_object_or_404(Item, pk=id)
    comment.date = datetime.now()
    comment.save()

    return HttpResponseRedirect(APP_URL + f'item/{id}')
