from django.contrib import admin
from .models import FraudActivity


@admin.register(FraudActivity)
class FraudActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_id', 'reason', 'detected_at')
    list_filter = ('detected_at', 'user')
    search_fields = ('user__email', 'reason')
