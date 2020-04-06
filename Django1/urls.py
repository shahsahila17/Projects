from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.amz,name="amz"),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('shop1',views.shop1,name='shop1'),
    path('utensils',views.utensils,name='utensils'),
    path('cloth',views.cloth,name='cloth'),
    path('sports1',views.sports1,name='sports1'),
    path('electronics',views.electronics,name='electronics'),

]