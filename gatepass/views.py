from unittest import loader

from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import redirect

import gatepass
from .forms import GatePassForm
from .models import GatePass


def index(request):
    #template = 'layout.html'
    return render(request,'layout.html')

def gatepass_list_view(request):
    template = 'gatepass_list_view.html'
    gatepass_list = GatePass.objects.all().order_by('transaction_date')
    return render(request, template, {'gatepass_list': gatepass_list})


def gatepass_create_view(request):
  if request.method == "POST":
    form = GatePassForm(request.POST)
    if not form.is_valid():
        return render(request, "layout.html", {"form": form})
    form.save()
    return HttpResponseRedirect("/gatepass/gatepass_list_view/")
  else:
      form = GatePassForm()

  return render(request, "layout.html", {"form": form})

def gatepass_report(request):
    # Filter by type, branch, date, or any criteria
    gatepass_type = request.GET.get('gatepass_type') # e.g., "Returnable" or "Non-Returnable"
    branch_id = request.GET.get('branch')  # Filter by branch ID
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Base QuerySet
    gatepasses = GatePass.objects.all()

    # Apply filters dynamically
    if gatepass_type:
        gatepasses = gatepasses.filter(gatepass_type=gatepass_type)
    if branch_id:
        gatepasses = gatepasses.filter(branch_id=branch_id)
    if start_date and end_date:
        gatepasses = gatepasses.filter(transaction_date__range=[start_date, end_date])

    # Render the report
    return render(request, 'gatepass_report.html', {'gatepasses': gatepasses})



