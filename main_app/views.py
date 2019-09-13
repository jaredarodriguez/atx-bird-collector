from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.views.generic import ListView, DetailView 
from .models import Bird, Trait 
from .forms import LocationForm

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age']
    

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
    bird = Bird.objects.get(id=bird_id)
    traits_bird_doesnt_have = Trait.objects.exclude(id__in = bird.traits.all().values_list('id'))
    location_form = LocationForm()
    return render(request, 'birds/detail.html', {
        'bird': bird, 'location_form': location_form,
        'traits': traits_bird_doesnt_have
  })

def add_location(request, bird_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.bird_id = bird_id
        new_location.save()
    return redirect('detail', bird_id=bird_id)

def assoc_trait(request, bird_id, trait_id):
    Bird.objects.get(id=bird_id).traits.add(trait_id)
    return redirect('detail', bird_id=bird_id)

class TraitList(ListView):
    model = Trait 

class TraitDetail(DetailView):
    model = Trait 

class TraitCreate(CreateView):
    model = Trait 
    fields = '__all__'

class TraitUpdate(UpdateView):
    model = Trait 
    fields = ['name', 'color']

class TraitDelete(DeleteView):
    model = Trait 
    success_url = '/traits/'