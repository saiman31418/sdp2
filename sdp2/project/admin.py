from django.contrib import admin

# Register your models here.
from .models import User, Appointment, Prescription, DoctorAdvice, Ambulance, Doctorregister, status, delay, cart, \
    Showcart

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(DoctorAdvice)
admin.site.register(Ambulance)
admin.site.register(Doctorregister)
admin.site.register(status)
admin.site.register(delay)
admin.site.register(cart)
admin.site.register(Showcart)
