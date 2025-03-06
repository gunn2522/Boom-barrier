from django import forms
from.models import GatePass


class GatePassForm(forms.ModelForm):
    class  Meta:
        model = GatePass
        Meta =forms.ModelChoiceField(queryset=GatePass.objects.all().order_by('transaction_date'),widget=forms.Select)
        fields = ['name','branch','voucher_type','gatepass_type','transaction_date','stock_date','vehicle','driver','expected_return_date','is_returned','actual_return_date','purpose','status']
