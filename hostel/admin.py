from django.contrib import admin
from .models import Room, Service

# Make admin list views user-friendly
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'capacity', 'rent', 'has_attached_washroom', 'is_available')
    list_filter = ('floor', 'capacity', 'has_attached_washroom', 'is_available')
    search_fields = ('room_number',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')
    search_fields = ('title',)
