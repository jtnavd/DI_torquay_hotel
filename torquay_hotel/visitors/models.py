from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)


class Rate(models.Model):
    nb_people = models.IntegerField()
    is_seaview = models.BooleanField()
    is_highseason = models.BooleanField()


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Room(models.Model):
    room_nb = models.SmallIntegerField(unique=True)
    rate_id = models.ForeignKey(Rate, on_delete = models.CASCADE)


class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)
    hotel_id = models.ForeignKey(Hotel, null=True, on_delete= models.PROTECT)
    room_id = models.ManyToManyField(Room)


class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    nationality = models.ForeignKey(Country, on_delete= models.PROTECT)
    passport_nb = models.CharField(max_length=20)
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()


class Booking(models.Model):
    """3 statuses:
    pending: as requested by guest
    confirmed: after review and room assignment by staff member
    canceled: by staff member"""
    start_day = models.DateField() # start of stay
    end_day = models.DurationField() # end of stay
    room_id = models.ManyToManyField(Room, related_name = 'rooms', blank=True)
    guest_id = models.ForeignKey(Guest, on_delete = models.CASCADE)
    status = models.CharField(max_length=10, default = 'pending')
    creation_date = models.DateTimeField(auto_now_add=True)
    confirmation_date = models.DateTimeField(null=True, blank=True)
    # confirmed_by = models.ForeignKey(Staff_user, on_delete=models.PROTECT)
    cancelation_date = models.DateTimeField(null=True, blank=True)
    # canceled_by = models.ForeignKey(Staff_user, on_delete=models.PROTECT)
    discount = models.FloatField(default = 0.)