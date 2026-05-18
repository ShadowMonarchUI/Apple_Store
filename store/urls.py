from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Cart
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    
    # Account
    path('orders/', views.my_orders, name='my_orders'),
    path('account/', views.account_settings, name='account_settings'),
    
    # Support
    path('help/', views.help_page, name='help'),
    path('contact/', views.contact_us, name='contact'),
]
