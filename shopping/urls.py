from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/$/', views.index, name='index'),
    path('update_item/', views.update_item_quantity, name='update_item_quantity'),
    path('thankyou/', views.thank_you, name='thankyou'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('cart/', views.cart, name='cart'),
    path('credit_card_page/', views.credit_card_page, name='credit_card_page'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]