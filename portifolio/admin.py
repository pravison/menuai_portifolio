from django.contrib import admin

from . models import Infor, Fact, Social_links, Service, Price, Promotion, Testimonial, Contact, Customer_acquistion, Contact_details
# Register your models here.

admin.site.register(Infor)
admin.site.register(Fact)
admin.site.register(Social_links)
admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Customer_acquistion)
admin.site.register(Contact_details)
admin.site.register(Promotion)