from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
admin.site.site_header = "Stock"
admin.site.index_title = "Stock"
admin.site.site_title = "Stock"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "grupo",
    )
    list_filter = (
        "groups",
    )
    search_fields = ["username", "first_name", "last_name", "email"]
    def grupo(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

class RoomAdmin(admin.ModelAdmin):
    list_display = (
    'quantity_beds',
    'room_number'
    )

class DoctorAdmin(admin.ModelAdmin):
    list_display = (
     "username",
        "email",
        "first_name",
        "last_name",
        "specialty"
    )
class CallAdmin(admin.ModelAdmin):
    list_display = (
        "state",
        "attendance_date",
        "creation_date",
        "user_create_call",
        "user_response_call",
    )

class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "weight",
        "room",
        "bloodType",
        "socialPlan",
        "height",
    )
    search_fields = ["username", "first_name", "last_name", "email"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BloodType)
admin.site.register(SocialPlan)
admin.site.register(Room,RoomAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Calls, CallAdmin)
admin.site.register(Patient,PatientAdmin)
