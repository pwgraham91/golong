from django.contrib import admin

# Register your models here.
from rideshare.models import Traveler, Car, Route

admin.site.register(Traveler)
admin.site.register(Car)
admin.site.register(Route)


