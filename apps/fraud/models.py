import uuid
from django.db import models
from django.contrib.auth import get_user_model
from apps.listings.models import Booking

User = get_user_model()

class FraudActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.reason}"