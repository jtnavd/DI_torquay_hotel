from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Prof_Guest(models.Model):
    pass

# class User(models.Model):
#     profile = models.ForeignKey(Staff)



