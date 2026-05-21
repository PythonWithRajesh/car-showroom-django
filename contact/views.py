from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        # 🔥 VALIDATION (empty check)
        if not name or not email or not mobile or not message:
            messages.error(request, "❌ Please fill all fields!")
            return redirect('contact')

        # 🔥 SAVE TO DATABASE
        Contact.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            message=message
        )

        messages.success(request, "✅ Message sent successfully!")
        return redirect('contact')

    return render(request, 'contact/contact.html')