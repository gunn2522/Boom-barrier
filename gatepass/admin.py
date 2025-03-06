from django.contrib import admin
from gatepass.models import GatePass,Branch,Vehicle,Driver

admin.site.register(GatePass)
list_display = ('name','branch','voucher_type','gatepass_type','transaction_date','stock_date','vehicle','driver', 'expected_return_date','is_returned','actual_return_date','purpose','status')
admin.site.register(Branch)
admin.site.register(Vehicle)
admin.site.register(Driver)



# Register your models here.
