from django.db import models

# Create your models here.
class Intro(models.Model):
    image= models.ImageField()
    tagline = models.CharField(max_length=100)
    sale_pitch = models.TextField(max_length=250)

    def __str__(self):
        return self.tagline

class About(models.Model):
    image= models.ImageField()
    short_description = models.TextField(max_length=500)
    long_description = models.TextField(max_length=500)

    def __str__(self):
        return f'id:  {self.id}'

class Social_links(models.Model):
    name = models.CharField(max_length=100)
    link =models.URLField()
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=100, default="bi bi-card-checklist") 
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f' send at {self.createdAt} by {self.name}'

class Values(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name

class Price(models.Model):
    plan = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    feature1 = models.CharField(max_length=100)
    feature2 = models.CharField(max_length=100, blank=True, null=True)
    feature3 = models.CharField(max_length=100, blank=True, null=True)
    feature4 = models.CharField(max_length=100, blank=True, null=True)
    feature5 = models.CharField(max_length=100, blank=True, null=True)
    feature6 = models.CharField(max_length=100, blank=True, null=True)
    feature7 = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.plan

class Aggrement(models.Model):
    title1 = models.CharField(max_length=100)
    paragraph1 = models.TextField(max_length=500, blank=True, null=True)
    paragraph2 = models.TextField(max_length=500, blank=True, null=True)
    paragraph3 = models.TextField(max_length=500, blank=True, null=True)
    title2 = models.CharField(max_length=100)
    paragraph4 = models.TextField(max_length=500, blank=True, null=True)
    title3 = models.CharField(max_length=100)
    paragraph5 = models.TextField(max_length=500, blank=True, null=True)
    paragraph6 = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title1
