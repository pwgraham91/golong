from django.db import models
from django.contrib.auth.models import AbstractUser

class Traveler(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222", null=True)
    age = models.IntegerField(max_length=2, null=True)
    background_checked = models.BooleanField(default=False)
    driver = models.BooleanField(help_text="Driver= True, Rider= False", default=False)
    traveler_image = models.ImageField(upload_to='traveler_images', null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.username)

class Car(models.Model):
    car_name = models.CharField(max_length=20, help_text="ex: Mr.T, Batmobile, Herbie, Green Hornet, Mystery Machine, Mad Max, Knight Rider")
    car_model = models.CharField(max_length=40, help_text="ex: Gray Nissan Altima")
    car_year = models.CharField(max_length=4, help_text="ex: 2008")
    seats = models.SmallIntegerField()
    owner = models.ForeignKey(Traveler, related_name='cars')
    car_image = models.ImageField(upload_to='car_images', null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.car_name)

class Route(models.Model):
    trip_name = models.CharField(max_length=30)
    start_city_state = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_city_state = models.CharField(max_length=50)
    end_date = models.DateTimeField()
    trip_driver = models.ForeignKey(Traveler, related_name="route_driver")
    trip_car = models.ForeignKey(Car, related_name="route_car")
    passenger = models.ManyToManyField(Traveler, related_name="route_passengers", null=True)

    def __unicode__(self):
        return u"{}".format(self.trip_name)
