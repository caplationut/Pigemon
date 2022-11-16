from django.shortcuts import render, redirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models import Count, Q
from .forms import *

# Create your views here.


def add_pigeon(request):
    if request.user.is_authenticated:
        translation.activate(request.user.language)
    else:
        return redirect('login')

    title = _("Add new pigeon")
    loft = Loft.objects.get(breeder=request.user)
    if request.method == "POST":
        form = AddPigeon(request.POST, breeder=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('index')
    else:
        form = AddPigeon(breeder=request.user)

    context = {
        'title': title,
        'lofts': loft,
        'form': form,
    }
    return render(request, "pigeon/add_pigeon.html", context)


def view_pigeons(request):
    if request.user.is_authenticated:
        translation.activate(request.user.language)
    else:
        return redirect('login')

    pigeons = Pigeon.objects.filter(loft__breeder=request.user).select_related('sire', 'dam').\
        prefetch_related('loft', 'color', 'status')
    total = pigeons.count()
    pigeons_count = pigeons.aggregate(male=Count('id', filter=Q(gender="MA")),
                                      female=Count('id', filter=Q(gender='FE')),
                                      unknown=Count('id', filter=Q(gender='NN')))
    title = _("View pigeons")
    loft = Loft.objects.get(breeder=request.user)

    context = {
        'title': title,
        'lofts': loft,
        'pigeons': pigeons,
        'total': total,
        'count': pigeons_count,
    }
    return render(request, "pigeon/pigeons.html", context)


def edit_pigeon(request, pk):
    if request.user.is_authenticated:
        translation.activate(request.user.language)
    else:
        return redirect('login')

    try:
        pigeon = Pigeon.objects.get(pk=pk)
    except Pigeon.DoesNotExist:
        messages.add_message(request, messages.WARNING,
                             _("The selected pigeon does not exist or has been deleted from the database."))
        return redirect('pigeons')
    if pigeon.loft.breeder != request.user:
        messages.add_message(request, messages.WARNING,
                             _("The pigeon with the ring , '{0}' does not exist or has been deleted!").
                             format(pigeon.ring_serial))
        return redirect('pigeons')

    if request.method == "POST":
        form = EditPigeon(request.POST, request.Files, breeder=request.user, instance=pigeon)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('index')
    else:
        form = EditPigeon(instance=pigeon, breeder=request.user)

    title = _("Update pigeon info")

    context = {
        'title': title,
        'pigeon': pigeon,
        'form': form,
    }

    return render(request, "pigeon/edit_pigeon.html", context)
