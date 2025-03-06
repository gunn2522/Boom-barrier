
from vehicle import admin
from vehicle import views
from django.urls  import path,include

urlpatterns = [
  path('', views.index, name='index'),
  path('vehicle_create_list/',views.vehicle_create_list, name='vehicle_create_list'),
  path('vehicle_list_view/',views.vehicle_list_view, name='vehicle_list_view'),
  path('fastag_create/',views.fastag_create, name='fastag_create'),
  path('fastag_list/',views.fastag_list,name='fastag_list'),

]