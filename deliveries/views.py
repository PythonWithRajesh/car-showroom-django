from django.shortcuts import render, redirect
from .models import Delivery
from .forms import DeliveryForm


def delivery_list(request):

    deliveries = Delivery.objects.all().order_by('-id')

    return render(request, 'deliveries/delivery_list.html', {
        'deliveries': deliveries
    })


def add_delivery(request):

    form = DeliveryForm()

    if request.method == 'POST':

        form = DeliveryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('deliveries')

    return render(request, 'deliveries/add_delivery.html', {
        'form': form
    })