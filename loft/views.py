from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext as _
from django.utils import translation
from django.utils import timezone
from .forms import *

# Create your views here.


class LoginPage(LoginView):
    """ Pagina autentificare"""
    template_name = "breeder/login.html"
    title = _("Sign in")
    current_year = timezone.now().year
    extra_context = {
        'year': current_year,
        'title': title,
    }


def new_loft(request):
    if request.user.is_authenticated:
        translation.activate(request.user.language)
        title = _("Add new loft")
        if request.method == "POST":
            form = AddLoft(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.breeder = request.user
                obj.save()
                return redirect('index')
        else:
            form = AddLoft()

        context = {
            'title': title,
            'form': form
        }
    return render(request, "loft/add_loft.html", context)
