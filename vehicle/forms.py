from django import forms
from.models import Vehicle
from.models import Fastag

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        Meta=forms.ModelChoiceField(queryset=Vehicle.objects.all().order_by('vehicle_type'))
        fields = ['vehicle_number', 'vehicle_type', 'owner_name','owner_contact','created_at','updated_at','fastag']


class FastagForm(forms.ModelForm):
    class Meta:
        model = Fastag
        Meta=forms.ModelChoiceField(queryset=Fastag.objects.all().order_by('fastag_id'))
        fields = ['fastag_id','fastag_balance','fastag_status','valid_till','created_at','updated_at']