from django.utils import timezone
from datetime import timedelta
from .models import FraudActivity
from apps.listings.models import Booking
from django.contrib.auth import get_user_model

User = get_user_model()

def detect_fraud(user, booking):
    reasons = []

    # Rule 1: Multiple bookings in a short time frame
    recent_bookings = Booking.objects.filter(
        user=user,
        created_at__gte=timezone.now() - timedelta(minutes=10)
    ).count()

    if recent_bookings > 3:
        reasons.append("Multiple bookings in a short period.")

    # Rule 2: Blacklisted email domains (example logic)
    blacklist_domains = ["fraudmail.com", "scammer.net"]
    if any(domain in user.email for domain in blacklist_domains):
        reasons.append("Blacklisted email domain detected.")

    # Rule 3: Location mismatch (placeholder example)
    if "New York" not in booking.property.address:
        reasons.append("Location mismatch detected.")

    # Log if any fraud reasons are found
    for reason in reasons:
        FraudActivity.objects.create(user=user, booking_id=booking.id, reason=reason)

    return reasons
