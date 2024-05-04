from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=200, default='Default Location')
    


    def __str__(self):
        return self.room_number
    
