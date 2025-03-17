from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from apps.listings.models import Booking
from ..listings.models import Booking
from .models import Payment
from .forms import CreditCardForm

# @login_required
# def make_payment(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             payment = form.save(commit=False)
#             payment.user = request.user
#             payment.booking = booking
#             payment.amount = booking.property.price_per_night  # Assume 1-night booking for simplicity
#             payment.status = 'pending'  # Initially mark it as pending
#             payment.save()
#
#             messages.success(request, "Payment is pending. Please verify through payment gateway.")
#             return redirect('listings:property_list')
#     else:
#         form = PaymentForm()
#
#     return render(request, 'payments/payment_success.html', {'form': form, 'booking': booking})


@login_required
def confirm_payment(request, booking_id):
    print(f"Received Booking ID from URL: {booking_id}")
    try:
        booking = Booking.objects.get(id=booking_id)
        print(f"Booking found: {booking}")
    except Booking.DoesNotExist:
        print("Booking not found in database!")
        raise

    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            # Simulate payment processing (replace with real gateway later)
            Payment.objects.create(
                user=request.user,
                booking=booking,
                amount=booking.property.price_per_night,
                payment_method='credit_card',
                status='completed'
            )
            messages.success(request, "Payment completed successfully!")
            return redirect('payments:payment_success')
        else:
            print("Payment Form Errors:", form.errors)
    else:
        form = CreditCardForm()

    return render(request, 'payments/confirm_payment.html', {'form': form, 'booking': booking})


@login_required
def payment_success(request):
    latest_payment = Payment.objects.filter(user=request.user).latest('created_at')
    return render(request, 'payments/payment_success.html', {'booking': latest_payment.booking})