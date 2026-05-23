from django.shortcuts import render, redirect
from .models import Car


def car_list(request):

    cars = Car.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'cars/car_list.html', context)


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