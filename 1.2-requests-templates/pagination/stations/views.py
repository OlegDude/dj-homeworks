from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(reader, 10)
    page = paginator.get_page(page_number)
    list_stations_page = paginator.page(page_number)
    context = {
         'bus_stations': list_stations_page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
