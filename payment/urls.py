from django.urls import path
from . import views

urlpatterns = [
	path('payment_success', views.payment_success, name="payment_success"),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name="billing_info"),
    path('shipped_dash', views.shipped_dash, name="shipped_dash"),
    path('process_order', views.process_order, name="process_order"),
    path('not_shipped_dash', views.not_shipped_dash, name="not_shipped_dash"),
    path('create_order', views.create_order, name="create_order"),
    path('orders/<int:pk>', views.orders, name='orders'),
]
