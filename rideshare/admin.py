from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from rideshare.models import Traveler, Car, Route

admin.site.register(Traveler, UserAdmin)
admin.site.register(Car)
admin.site.register(Route)


