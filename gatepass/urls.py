from gatepass import admin
from gatepass import views
from django.urls  import path,include


from gatepass.views import  index


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', index, name='index'),
    #path('gatepass_list/', gatepass_list_view, name='gatepass_list'),
    path('gatepass_create_view/', views.gatepass_create_view, name='gatepass_create_view'),
    path('gatepass_list_view/', views.gatepass_list_view, name='gatepass_list_view'),
    path('gatepass-report/', views.gatepass_report, name='gatepass_report'),




]


