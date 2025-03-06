from django.db import models
from gatepass.models import Vehicle

class Fastag(models.Model):
    fastag_id = models.CharField(max_length=50, unique=True)  # Unique ID for the Fastag
    fastag_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Balance in the Fastag account
    fastag_status = models.CharField(max_length=20, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('BLOCKED', 'Blocked')], default='ACTIVE')
    valid_till = models.DateField()  # Expiry date for the Fastag
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)


class Vehicle(models.Model):
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE,related_name='Vehicle')  # Vehicle registration number (e.g., MH12AB1234)
    vehicle_type = models.CharField(max_length=50, choices=[('CAR', 'Car'), ('TRUCK', 'Truck'), ('BUS', 'Bus'), ('MOTORCYCLE', 'Motorcycle')])
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fastag= models.ForeignKey(Fastag, on_delete=models.CASCADE,related_name='Vehicle')

    class Meta:
        ordering = ['vehicle_number']

    def __str__(self):
        return f"{self.fastag_id} ({self.fastag_balance})"
    

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"
