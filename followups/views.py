from django.shortcuts import render, redirect
from .models import Followup
from .forms import FollowupForm


def followup_list(request):

    followups = Followup.objects.all()

    context = {

        'followups': followups

    }

    return render(request,
        'followups/followup_list.html',
        context)



def add_followup(request):

    form = FollowupForm()

    if request.method == 'POST':

        form = FollowupForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('followups')

    context = {

        'form': form

    }

    return render(request,
        'followups/add_followup.html',
        context)