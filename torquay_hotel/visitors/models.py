from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Room(models.Model):
    nb_people = models.IntegerField()
    is_seaview = models.BooleanField()


class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/', null = True, blank = True)
    hotel_id = models.ForeignKey(Hotel, null = True,  on_delete = models.PROTECT)
    room_id = models.ManyToManyField(Room, null = True, on_delete = models.PROTECT)


class BookedDate(models.Model):
    """Date on which a room is booked"""
    booked_day = models.DateField()
    duration = models.DurationField()
    room_id = models.ManyToManyField(Room, related_name = 'rooms')
    # guest_id = 
    # created_by = 
    # modified_by =
    # creation_date =


class RequestedDate(models.Model):
    """Date on which a room is requested by a customer"""
    pass


class Rate(models.Model):
    pass


class Guest(models.Model):
    pass