from django.db import models
from django.urls import reverse
from datetime import date 

LOCATIONS = (
    ('N', 'North'),
    ('S', 'South'),
    ('E', 'East'),
    ('W', 'West')
)

class Trait(models.Model):
    name = models.CharField(max_length=50)
    color= models.CharField(max_length=20)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('traits_detail', kwargs={'pk': self.id})

class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    traits = models.ManyToManyField(Trait)

    def __str__(self): 
        return self.name 
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

class Location(models.Model):
    date = models.DateField('location date')
    location = models.CharField(
        max_length=1, 
        choices=LOCATIONS, 
        default=LOCATIONS[0][0]
    )
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} on {self.date}" 

    class Meta:
        ordering = ['-date']
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bird_id: {self.bird_id} @{self.url}"


