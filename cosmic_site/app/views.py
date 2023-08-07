from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import *


def home_page(request):
    return render(request, 'app/base.html', {'is_auth': request.user.is_authenticated})


def interesing_facts_page(request):
    data = Facts.objects.all()
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/interesing_fact.html', {'page_obj': page_obj, 'is_auth': request.user.is_authenticated, 'data': data})


def info_page(request):
    return render(request, 'app/info.html')


def contacts_page(request):
    return render(request, 'app/contacts.html', {'is_auth': request.user.is_authenticated})


def asteroid_page(request):
    return render(request, 'app/asteroid.html', {'is_auth': request.user.is_authenticated})


def planet_page(request):
    return render(request, 'app/planet.html', {'is_auth': request.user.is_authenticated})


def star_page(request):
    return render(request, 'app/star.html', {'is_auth': request.user.is_authenticated})


def nebula_page(request):
    return render(request, 'app/nebula.html', {'is_auth': request.user.is_authenticated})


def galaxy_page(request):
    return render(request, 'app/galaxy.html', {'is_auth': request.user.is_authenticated})


def black_hole_page(request):
    return render(request, 'app/black_hole.html', {'is_auth': request.user.is_authenticated})


def space_time_page(request):
    return render(request, 'app/space_time.html', {'is_auth': request.user.is_authenticated})


def dark_energy_page(request):
    return render(request, 'app/dark_energy.html', {'is_auth': request.user.is_authenticated})


def universe_page(request):
    return render(request, 'app/universe.html', {'is_auth': request.user.is_authenticated})


def page_not_found(request, exception):
    HttpResponseNotFound("<h1>Страница не найдена :/<br>Error 404</h1>")


def add_fact(request):
    if request.method == 'POST':
        form = AddFactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddFactForm()

    return render(request, 'app/add_fact.html', {'form': form, 'is_auth': request.user.is_authenticated})


def sign_in(request):
    return redirect('admin/')