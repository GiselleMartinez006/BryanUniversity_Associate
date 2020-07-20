from django.shortcuts import render
from django.views import generic
from .models import Location


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        return Location.objects.order_by('-created_on')[:20]



class DetailView(generic.DetailView):
    model= Location
    template_name = 'home/detail.html'
    context_object_name = 'location'