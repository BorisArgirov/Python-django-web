from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destination.models import Destination


def index(request):
    return HttpResponse("Welcom to our travel aplication!")

def destinations_list(request):
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations,
        'page_title': 'All Destinations'
    }

    return render(request, 'destination/list.html', context)

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination,
        'page_title': f"{destination.name} Details",
    }

    return render(request, 'destination/detail.html', context)

def redirect_home(request):
    return redirect('list')

