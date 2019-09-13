from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.views.generic import ListView, DetailView 

import boto3
import uuid

from .models import Bird, Trait, Photo 
from .forms import LocationForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'atxbirdcollector'

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

def unassoc_trait(request, bird_id, trait_id):
    Bird.objects.get(id=bird_id).traits.remove(trait_id)
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

def add_photo(request, bird_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file: 
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, bird_id=bird_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', bird_id=bird_id)

