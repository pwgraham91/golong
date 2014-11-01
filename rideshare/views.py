from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.files.uploadhandler import FileUploadHandler
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from rideshare.forms import TravelerUserCreationForm, CarForm, RouteForm
from models import Route, Traveler, Car


def home(request):
    routes = Route.objects.all()
    data = {
        'routes': routes,
    }
    return render(request, 'home.html', data)

def register(request):
    if request.method == 'POST':
        form = TravelerUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect("/")
    else:
        form = TravelerUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required()
def profile(request):
    routes = Route.objects.filter(trip_driver__username=request.user)
    passenger_routes = Route.objects.filter(passenger__username=request.user)
    cars = Car.objects.filter(owner__username=request.user)
    data = {
        'traveler': request.user,
        'routes': routes,
        'cars': cars,
        'passenger_routes': passenger_routes,
    }
    return render(request, 'profile.html', data)

@login_required()
def car_form(request):
    data = {"car_form": CarForm()}
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            Car.objects.create(car_name=form.cleaned_data['car_name'],
                               car_model=form.cleaned_data['car_model'],
                               car_year=form.cleaned_data['car_year'],
                               seats=form.cleaned_data['seats'],
                               car_image=form.cleaned_data['car_image'],
                               owner=request.user)
            routes = Route.objects.filter(trip_driver__username=request.user)
            passenger_routes = Route.objects.filter(passenger__username=request.user)
            cars = Car.objects.filter(owner__username=request.user)
            data = {
                'traveler': request.user,
                'routes': routes,
                'cars': cars,
                'passenger_routes': passenger_routes,
            }
            return render(request, "profile.html", data)
        else:
            data = {"car_form": form}
            return render(request, "car_form.html", data)

    else:
        return render(request, "car_form.html", data)

@login_required()
def route_form(request):
    traveler = request.user
    data = {"route_form": RouteForm(traveler= traveler)}
    # route_form = RouteForm()
    if request.method == 'POST':
        form = RouteForm(request.POST, traveler=traveler)
        if form.is_valid():
            Route.objects.create(trip_name=form.cleaned_data['trip_name'],
                               start_city_state=form.cleaned_data['start_city_state'],
                               start_date=form.cleaned_data['end_date'],
                               end_city_state=form.cleaned_data['end_city_state'],
                               end_date=form.cleaned_data['end_date'],
                               trip_driver= request.user,
                               trip_car=form.cleaned_data['trip_car'])
            return render(request, "home.html")

        else:
            data = {"route_form": form}
            return render(request, "route_form.html", data)
    else:
        return render(request, "route_form.html", data)

def view_car(request, car_id):
    car = Car.objects.get(id=car_id)
    data = {"car": car}
    return render(request, "view_car.html", data)

def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    data = {"car_form": CarForm()}
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            Car.objects.create(car_name=form.cleaned_data['car_name'],
                               car_model=form.cleaned_data['car_model'],
                               car_year=form.cleaned_data['car_year'],
                               seats=form.cleaned_data['seats'],
                               car_image=form.cleaned_data['car_image'],
                               owner=request.user)
            car.delete()
            routes = Route.objects.filter(trip_driver__username=request.user)
            passenger_routes = Route.objects.filter(passenger__username=request.user)
            cars = Car.objects.filter(owner__username=request.user)
            data = {
                'traveler': request.user,
                'routes': routes,
                'cars': cars,
                'passenger_routes': passenger_routes,
            }
            return render(request, "profile.html", data)
        else:
            data = {"car_form": form}
            return render(request, "car_form.html", data)

    else:
        return render(request, "car_form.html", data)

def view_route(request, route_id):
    viewer = request.user
    route = Route.objects.get(id=route_id)
    data = {"route": route, "viewer": viewer}
    return render(request, "view_route.html", data)

def edit_route(request, route_id):
    route = Route.objects.get(id=route_id)
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            Route.objects.create(trip_name=form.cleaned_data['trip_name'],
                               start_city_state=form.cleaned_data['start_city_state'],
                               start_date=form.cleaned_data['end_date'],
                               end_city_state=form.cleaned_data['end_city_state'],
                               end_date=form.cleaned_data['end_date'],
                               trip_driver= request.user,
                               trip_car=form.cleaned_data['trip_car'])
            route.delete()
            return redirect("profile")
    else:
        form= RouteForm()
    data = {"route": route, "form": form}
    return render(request, "edit_route.html", data)

def view_traveler(request, traveler_id):
    traveler = Traveler.objects.get(id=traveler_id)
    routes = Route.objects.filter(trip_driver__id=traveler_id)
    passenger_routes = Route.objects.filter(passenger__id=traveler_id)
    data = {"traveler": traveler, "routes": routes, "passenger_routes": passenger_routes}
    return render(request, "view_traveler.html", data)

def delete_route(request, route_id):
    route = Route.objects.get(id=route_id)
    route.delete()
    return redirect("profile")

def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect("profile")