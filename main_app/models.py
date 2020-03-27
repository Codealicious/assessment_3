from django.db import models
from django.urls import reverse

class Wish(models.Model):
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name + str(self.quantity)



