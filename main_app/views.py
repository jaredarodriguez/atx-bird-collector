from django.shortcuts import render

class Bird: 
    def __init__(self, name, breed, description, age): 
        self.name = name 
        self.breed = breed
        self.description = description
        self.age = age 

birds = [
    Bird('Jojo', 'monk parrot', 'bright green', 4), 
    Bird('Marion', 'pidgeon', 'toxic grey', 3), 
    Bird('Mud', 'barn swallow', 'orange belly', 5)
]

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', {'birds': birds})