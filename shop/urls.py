from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='ShopHome'),
    path('about/',views.about, name='AboutUS'),
    path('contact/',views.contact, name='ContactUS'),
    path('tracker/',views.tracker, name='TrackingStatus'),
    path('search/',views.search, name='Search'),
    path('productview/<int:myid>',views.productView, name='ProductView'),
    path('checkout/',views.checkout, name='Checkout'),
    path('handlerequest/', views.handlerequest, name="HandleRequest")
]
