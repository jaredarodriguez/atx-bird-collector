from django.contrib import admin
from .models import Bird, Location, Photo

# Register your models here.

admin.site.register(Bird)
admin.site.register(Location)
admin.site.register(Photo)