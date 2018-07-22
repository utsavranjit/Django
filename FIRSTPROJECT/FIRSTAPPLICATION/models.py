from django.db import models

# Create your models here.

class Name_ID(models.Model):
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    nam = models.ForeignKey(Name_ID)
    contact = models.CharField(max_length=264, unique= True)

    def __str__(self):
        return self.contact

class Address(models.Model):
    con=models.ForeignKey(Contact)
    addr = models.CharField(max_length=264)

    def __str__(self):
        return self.addr
