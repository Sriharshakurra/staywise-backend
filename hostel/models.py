from django.db import models

class Room(models.Model):
    floor = models.IntegerField()
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} (Floor {self.floor})"

# 👇 New Model for Customer-Facing Services
class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Optional short description of the service.")
    icon_class = models.CharField(max_length=50, blank=True, help_text="Optional icon or emoji.")

    def __str__(self):
        return self.title
