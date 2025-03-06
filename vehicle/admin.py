from django.contrib import admin

from vehicle.models import Vehicle,Fastag


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_type', 'owner_name','owner_contact','created_at','updated_at','fastag')
    search_fields = ['vehicle_number']

class FastagAdmin(admin.ModelAdmin):
    list_display = ('fastag_id','fastag_balance','fastag_status','valid_till','created_at','updated_at')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Fastag)


# Register your models here.
