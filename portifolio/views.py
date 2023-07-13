from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Infor, Fact, Social_links, Service, Testimonial , Price , Promotion, Customer_acquistion, Contact_details, Contact



# Create your views here.

def index(request):
    infors = Infor.objects.order_by('-updatedAt')[:1]
    facts = Fact.objects.order_by('-updatedAt')[:1]
    links = Social_links.objects.order_by('-updatedAt')[:1]
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    prices = Price.objects.order_by('-updatedAt')[:1]
    acquistions = Customer_acquistion.objects.order_by('-updatedAt')[:1]
    contacts = Contact_details.objects.order_by('-updatedAt')[:1]
    promotions = Promotion.objects.order_by('-createdAt')[:1]

    quota=[]
    annual= []
    for price in prices:
        quota = (price.priceQuartely - price.priceMonthly)*(-12)
        annual = (price.priceYearly - price.priceMonthly)*(-12)

    context = {
        "infors": infors,
        "facts" : facts,
        "links":links,
        "services": services,
        "testimonials": testimonials,
        "prices": prices,
        "promtions": promotions,
        "acquistions":acquistions,
        "contacts": contacts,
        "quota": quota,
        "annual": annual,
        
    }
    return render(request, "index.html", context)


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
    
def sale(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        location = request.POST['location']
        contact = Contact(name=name, phone=phone, location=location)

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('home')


