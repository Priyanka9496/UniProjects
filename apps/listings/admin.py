from django.contrib import admin
from .models import Property  # Ensure you import the model correctly


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'price_per_night', 'available', 'is_verified', 'created_at')
    list_display_links = ('title',)  # Make 'title' clickable to the detail page
    search_fields = ('title', 'address')
    list_filter = ('available', 'is_verified', 'created_at')
    list_editable = ('is_verified',)  # Allow inline editing for 'is_verified'
