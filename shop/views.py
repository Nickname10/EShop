from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from .models import Item, Comment, Category

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


def index(request):
    return render(request, "index.html",
                  context={"Items": Item.objects.all()[0:9],
                           "User": request.user,
                           "Categories": Category.objects.all(),
                           })


def showItems(request):
    result_response = Item.objects.all()
    if request.GET.get("New") == "true":
        result_response = result_response.filter(isNewCollection=True)
    if request.GET.get("Discount") == "true":
        print("filter Discount")
        result_response = result_response.filter(discount_price=not None)
    if request.GET.getlist("Brand")[0] != '':
        print(request.GET.getlist("Brand"))
        result_response = result_response.filter(Brand__in=request.GET.getlist("Brand"))
    if request.GET.getlist("Sizes")[0] != '':
        result_response = result_response.filter(sizeandavailable__foot_size__in=request.GET.getlist("Sizes"))
    page = int(request.GET.get("Page"))
    print("PAGEEEE " + str(page))
    return JsonResponse({'Items': list(
        result_response.values('id', 'title', 'image','Brand', 'short_description','long_description', 'price')[page * 9:(page + 1) * 9])})


def showNext(request, page):
    print(page)

    return JsonResponse(
        {'Items': list(
            Item.objects.all().values('id', 'title', 'image', 'short_description', 'price')[page * 10:(page + 1) * 10])}
    )


def showItem(request, id):
    for i in Item.objects.all():
        print(i.id)
    return render(request, 'about_item.html',
                  context={"Item": Item.objects.all().filter(id=id)[0],
                           "User": request.user,
                           "Comments": Comment.objects.filter(item_id=id)})


def addComment(request, id):
    comment = Comment()
    comment.user = request.user
    comment.text = request.POST['message']
    comment.item = get_object_or_404(Item, pk=id)
    comment.date = datetime.now()
    comment.save()

    return HttpResponseRedirect(APP_URL + f'item/{id}')


def addItemToOrder(request, id):
    pass
