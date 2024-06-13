from django.urls import path
from . import views

urlpatterns = [
    path('companies/<str:companyname>/categories/<str:categoryname>/products', views.get_top_products, name='get_top_products'),
]
