from django.shortcuts import render , redirect
from django.contrib import messages
from . models import *
# Create your views here.
def home(request):
    intros = Intro.objects.all()
    abouts = About.objects.all()
    links = Social_links.objects.all()
    services = Service.objects.all()
    values = Values.objects.all()
    prices = Price.objects.all()
    context = {
        'intros': intros,
        'abouts': abouts,
        'links': links,
        'services': services,
        'values': values,
        'prices': prices       
    }
    return render(request, "menuai/index.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, phone=phone, subject=subject, message=message,)

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('home')

def terms(request):
    intros = Intro.objects.all()
    aggrements = Aggrement.objects.all()
    links = Social_links.objects.all()
    services = Service.objects.all()
    context={
        'intros': intros,
        'aggrements': aggrements,
        'links': links,
        'services': services,
    }
    return render(request, 'menuai/terms_of_service.html', context)