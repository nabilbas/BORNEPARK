from django.urls import path
from .views import user_list, borne_list, ombriere_list, home, Item_TRYDAN
from . import views

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('products/', views.products_view, name='products'),
    path('', home, name='home'),
    path('Item_TRYDAN/', Item_TRYDAN, name='Item_TRYDAN'),
]
