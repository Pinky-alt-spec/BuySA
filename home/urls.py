from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name="shop"),
    path('404', views.fof, name="404"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('terms&conditions', views.tcs, name="terms&conditions"),
    path('faq', views.faq, name="faq"),
    path('cart', views.cart, name="cart"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('checkout', views.checkout, name="checkout"),


]
