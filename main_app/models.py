from django.db import models
from django.urls import reverse

LOCATIONS = (
    ('N', 'North'),
    ('S', 'South'),
    ('E', 'East'),
    ('W', 'West')
)


class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self): 
        return f'{self.name} ({self.id})' 
    
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
    


