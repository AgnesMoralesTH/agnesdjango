from django.urls import path
from .views import Home, Shop, Contact

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('shop/', Shop.as_view(), name="shop" ),
    path('contact/', Contact.as_view(), name="contact"),
]