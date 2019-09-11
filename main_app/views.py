from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from .models import Bird 
from .forms import LocationForm

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id = bird_id)
    location_form = LocationForm()
    return render(request, 'birds/detail.html', {'bird': bird, 'location_form': location_form})

def add_location(request, bird_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.bird_id = bird_id
        new_location.save()
    return redirect('detail', bird_id=bird_id)

