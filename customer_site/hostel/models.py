from django.db import models

# Room model including floor, capacity, price, and washroom info
class Room(models.Model):
    floor = models.PositiveIntegerField()
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    rent = models.PositiveIntegerField(help_text="Monthly rent in INR")
    has_attached_washroom = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} (Floor {self.floor})"


# Service model shown to users on the public site
class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Short description of the service")
    icon_class = models.CharField(max_length=50, blank=True, help_text="Optional icon or emoji")

    def __str__(self):
        return self.title
