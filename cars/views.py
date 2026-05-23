from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car


@login_required(login_url='/')
def car_list(request):

    cars = Car.objects.all()

    return render(request, 'cars/car_list.html', {
        'cars': cars
    })


@login_required(login_url='/')
def add_car(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        price = request.POST.get('price')
        mileage = request.POST.get('mileage')
        image = request.FILES.get('image')

        Car.objects.create(
            name=name,
            price=price,
            mileage=mileage,
            image=image
        )

        return redirect('cars')

    return render(request, 'cars/add_car.html')