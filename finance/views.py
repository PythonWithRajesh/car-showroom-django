from django.shortcuts import render, redirect
from .models import Finance
from .forms import FinanceForm

def finance_list(request):

    finances = Finance.objects.all().order_by('-id')

    return render(request, 'finance/finance_list.html', {
        'finances': finances
    })


def add_finance(request):

    form = FinanceForm()

    if request.method == 'POST':

        form = FinanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('finance')

    return render(request, 'finance/add_finance.html', {
        'form': form
    })