from django.urls import path
from . import views as service_views

urlpatterns = [
    path('', service_views.services, name='services'),
]