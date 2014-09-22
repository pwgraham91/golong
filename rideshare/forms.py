from django.contrib.auth.forms import UserCreationForm
from rideshare.models import Traveler, Car, Route
from django import forms


class TravelerUserCreationForm(UserCreationForm):
    class Meta:
        model = Traveler
        fields = ("username", "first_name", "last_name", "age", "phone", "password1", "password2", "email", "traveler_image")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Traveler.objects.get(username=username)
        except Traveler.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

#
# class RouteForm(forms.Form):
#     trip_name = forms.CharField(label="Trip Name")
#     start_city_state = forms.CharField(label="Departing City")
#     start_date = forms.DateTimeField(label="Date and Time you will be departing")
#     end_city_state = forms.CharField(label="Arrival City")
#     end_date = forms.DateTimeField(label="Date and Time you plan on arriving")
#     trip_car = forms.ModelChoiceField(queryset=Car.objects.all(), label="Car you will be taking on the trip")
#     passenger = forms.ModelMultipleChoiceField(queryset=Traveler.objects.all(), label="Passenger(s) riding with you")

class RouteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        traveler = kwargs.pop('traveler', None)
        super(RouteForm, self).__init__(*args, **kwargs)
        self.fields['trip_car'] = forms.ModelChoiceField(Car.objects.filter(owner=traveler))
    class Meta:
        model = Route
        fields = ("trip_name", "start_city_state", "start_date",
                  "end_city_state", "end_date", "trip_car", "passenger")

class CarForm(forms.Form):
    car_name = forms.CharField(label="Car Name: ex: Mr.T, Batmobile, Herbie, Green Hornet, Mystery Machine, Mad Max, Knight Rider, General Lee, The Magic Schoolbus")
    car_model = forms.CharField(label="Car model: ex: Gray Nissan Altima")
    car_year = forms.IntegerField(label="Model Year: ex: 2008")
    seats = forms.IntegerField()
    car_image = forms.ImageField(label="picture of your car")
