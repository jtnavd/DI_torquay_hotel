from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class BookingCheck(models.Model):
    client_id = models.ForeignKey()
    room_id = models.ManyToManyField()
    room_type = models.ManyToManyField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()    

class BookingApproved(models.Model):
    pass

class CancelledBooking(models.Model):
    pass

class Customer(models.Model):
    profile = models.ForeignKey()
    # client_id = 
    # client_name = 
    client_message = models.ForeignKey()



