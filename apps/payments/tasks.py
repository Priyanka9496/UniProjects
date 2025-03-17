from celery import shared_task
from .models import Payment


@shared_task
def verify_payment(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        # Example: AI fraud detection logic can be added here.
        if float(payment.amount) > 1000:  # Dummy threshold for demonstration.
            payment.status = 'flagged'
        else:
            payment.status = 'completed'
        payment.save()
    except Payment.DoesNotExist:
        pass
