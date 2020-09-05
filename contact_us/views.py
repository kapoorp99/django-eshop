from django.shortcuts import render
from .models import ContactUsForm
from datetime import datetime
from django.contrib import messages


# Create your views here.
def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('problem_description')
        contact = ContactUsForm(
            name=name,
            email=email,
            phone=phone,
            description=description,
            timestamp=datetime.today()
        )
        contact.save()
        messages.success(request, 'Your complaint has been registered.')

    return render(request, 'contact_us/contact_us.html')
