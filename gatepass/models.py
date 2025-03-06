# from django.db import models
#
#
# class driver(models.Model):
#     driver_name = models.CharField(max_length=100)
#     contact_number = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.driver_name}"
#
# class vehicle(models.Model):
#     vehicle_number = models.CharField(max_length=11)
#     vehicle_colour = models.CharField(max_length=11)
#
# class Branch(models.Model):
#     name = models.CharField(max_length=100)
#     branch = models.CharField(max_length=100 ,default="")
#
#
# class GatePass(models.Model):
#     name = models.CharField(max_length=100)
#     branch =  models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='gatepass')
#     voucher_type = models.CharField(max_length=100)
#     gatepass_type = models.CharField(max_length=100)
#     transaction_date = models.DateField()
#     stock_date = models.DateField()
#     vehicle= models.ForeignKey(vehicle,on_delete=models.CASCADE,related_name='gatepass')
#     driver= models.ForeignKey(driver,on_delete=models.CASCADE,related_name='gatepass')
#
#
#
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __str__(self):
#         return f"{self.name}"

from django.db import models


# Driver Model
class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)

    def __str__(self):
        return self.driver_name


# Vehicle Model
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=11)
    vehicle_colour = models.CharField(max_length=11)

    def __str__(self):
        return self.vehicle_number


# Branch Model
class Branch(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


# GatePass Model
class GatePass(models.Model):
    # GatePass Types
    RETURNABLE = 'Returnable'
    NON_RETURNABLE = 'Non-Returnable'

    GATEPASS_TYPE_CHOICES = [
        (RETURNABLE, 'Returnable'),
        (NON_RETURNABLE, 'Non-Returnable'),
    ]

    # Core Fields
    name = models.CharField(max_length=100)  # Gate Pass Name or Identifier
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='gatepass')  # Branch Details
    voucher_type = models.CharField(max_length=100)  # Voucher Type (e.g., Sales, Purchase)
    gatepass_type = models.CharField(max_length=20, choices=GATEPASS_TYPE_CHOICES)  # Returnable or Non-Returnable
    transaction_date = models.DateTimeField(blank=True, null=True)  # Date of GatePass Transaction
    stock_date = models.DateField(blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='gatepass')  # Vehicle Details
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='gatepass')  # Driver Details

    # Additional Fields for Returnable Gate Pass
    expected_return_date = models.DateField(blank=True, null=True)  # Expected Return Date
    is_returned = models.BooleanField(default=False)  # Has the item been returned?
    actual_return_date = models.DateField(blank=True, null=True)  # Actual Return Date (if applicable)

    # Additional Fields
    purpose = models.TextField(blank=True, null=True)  # Reason for the GatePass
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
        default='Pending'
    )  # Status of the GatePass

    def __str__(self):
        return f"{self.name} - {self.gatepass_type}"

    def mark_as_returned(self):
        """Mark the Gate Pass as returned and set the actual return date."""
        if self.gatepass_type == self.RETURNABLE:
            self.is_returned = True
            self.actual_return_date = models.DateField(auto_now=True)
            self.status = 'Completed'
            self.save()

    class Meta:
        ordering = ['-transaction_date']



# Create your models here.
