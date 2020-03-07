from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from .models import Item

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
    return render(request, "index.html", context={"Items": Item.objects.all()[:10], "User": request.user})


def showNext(request, page):
    print(page)

    return JsonResponse(
        {'Items': list(
            Item.objects.all().values('title', 'image', 'short_description', 'price')[page * 10:(page + 1) * 10])}
    )


def showItem(request, id):
    for i in Item.objects.all():
        print(i.id)
    return render(request, 'about_item.html', context={"Item": Item.objects.all().filter(id=id)[0]})
