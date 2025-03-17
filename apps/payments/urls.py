from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('confirm/<uuid:booking_id>/', views.confirm_payment, name='confirm_payment'),
    path('success/', views.payment_success, name='payment_success'),
]
