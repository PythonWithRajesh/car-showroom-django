from django.shortcuts import render
from customers.models import Customer
from cars.models import Car
from followups.models import Followup

def reports_dashboard(request):
    total_customers = Customer.objects.count()
    total_cars = Car.objects.count()
    total_followups = Followup.objects.count()

    pending_followups = Followup.objects.filter(status='Pending').count()

    recent_customers = Customer.objects.all().order_by('-id')[:5]
    recent_followups = Followup.objects.all().order_by('-id')[:5]

    context = {
        'total_customers': total_customers,
        'total_cars': total_cars,
        'total_followups': total_followups,
        'pending_followups': pending_followups,
        'recent_customers': recent_customers,
        'recent_followups': recent_followups,
    }

    return render(request, 'reports/dashboard.html', context)