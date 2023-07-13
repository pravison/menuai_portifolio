from django.db import models

# Create your models here.
class  Infor(models.Model):
    companyName = models.CharField(max_length=200)
    teamsPhoto = models.ImageField()
    overview = models.TextField(max_length=500)
    description = models.TextField(max_length=1000)
    totalCustomers = models.IntegerField()
    promotion_message = models.TextField(max_length=500, blank=True)
    customersEnrolled = models.CharField(max_length=15, blank=True)
    percentage = models.CharField(max_length=50, blank=True)
    payment_till = models.IntegerField(default='0740562740')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.companyName
    
class Social_links(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    skype = models.URLField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'updated at {self.updatedAt}'
    
class Fact(models.Model):
    totalClients = models.IntegerField()
    projects = models.IntegerField()
    hoursSupport = models.IntegerField()
    totalTeam = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'updated at {self.updatedAt}'
    
class Service(models.Model):
    serviceName = models.CharField(max_length=30)
    icon = models.CharField(max_length=100, default="bi bi-card-checklist") 
    image = models.ImageField( blank=True)
    serviceDescription = models.TextField(max_length=500)

    def __str__(self):
        return self.serviceName

class Services_offerd(models.Model):
    service1 = models.CharField(max_length=30)
    description1 = models.TextField(max_length=500)
    service2 = models.CharField(max_length=30)
    description2 = models.TextField(max_length=500)
    service3 = models.CharField(max_length=30)
    description3 = models.TextField(max_length=500)
    service4 = models.CharField(max_length=30)
    description4 = models.TextField(max_length=500)
    service5 = models.CharField(max_length=30)
    description5 = models.TextField(max_length=500)
    service6 = models.CharField(max_length=30)
    description6 = models.TextField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'services offered {self.createdAt}'
    

class Price(models.Model):
    priceMonthly = models.IntegerField()
    priceQuartely = models.IntegerField()
    priceYearly = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'updated at {self.updatedAt}'

class Testimonial(models.Model):
    customerName = models.CharField(max_length=100)
    customerPhoto = models.ImageField()
    customerJobPosition = models.CharField(max_length=100)
    CustomerMessage = models.TextField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.customerName
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Customer_acquistion(models.Model):
    monthly = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'updated at {self.updatedAt}'

class Contact_details(models.Model):
    call = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'updated at {self.updatedAt}'


class Sales(models.Model):
    name= models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} enquired at {self.updatedAt}'
    
class Promotion(models.Model):
    message= models.TextField(max_length=100)
    customersEnrolled = models.CharField(max_length=15)
    percentage = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customers_enrolled} clients enrolled {self.percentage}% of the expected'

