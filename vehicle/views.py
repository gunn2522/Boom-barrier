from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import redirect

import gatepass
from .forms import Vehicle, VehicleForm, FastagForm
from .models import Vehicle
from .models import Fastag



def index(request):
    return render(request, 'vehicle_create_list.html')



def vehicle_create_list(request):
  if request.method == "POST":
    form = VehicleForm(request.POST)
    if  form.is_valid():
        form.save()
        return HttpResponseRedirect("/vehicle/vehicle_list_view/")

    return render(request, "vehicle_list_view", {'form': form})

  else:
      form = VehicleForm()

  return render(request, "vehicle_create_list.html", {"form": form})


def vehicle_list_view(request):
    template = 'vehicle_list_view.html'
    vehicle_list = Vehicle.objects.all().order_by('vehicle_type')
    return render(request, template, {'vehicle_list': vehicle_list})


#fastag views

def fastag_create(request):
  if request.method == "POST":
    form = FastagForm(request.POST)
    if  form.is_valid():
        form.save()
        return HttpResponseRedirect("/vehicle/fastag_list/")

    return render(request, "fastag_list.html", {"form": form})


  else:
      form = FastagForm()

  return render(request, "fastag_create.html", {"form": form})



def fastag_list(request):
    template = 'fastag_list.html'
    fastag_list = Fastag.objects.all().order_by('fastag_id')
    return render(request, template, {'fastag_list': fastag_list})










# Create your views here.
