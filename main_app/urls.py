from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'), 
    path('birds/', views.birds_index, name='index'), 
    path('birds/<int:bird_id>', views.birds_detail, name='detail'), 
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'), 
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'),
    path('birds/<int:bird_id>/add_location/', views.add_location, name='add_location'),
    path('birds/<int:bird_id>/assoc_trait/<int:trait_id>/', views.assoc_trait, name='assoc_trait'),
    path('birds/<int:bird_id>/unassoc_trait/<int:trait_id>/', views.unassoc_trait, name='unassoc_trait'),
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
    path('traits/', views.TraitList.as_view(), name='traits_index'),
    path('traits/<int:pk>/', views.TraitDetail.as_view(), name='traits_detail'),
    path('traits/create/', views.TraitCreate.as_view(), name='traits_create'),
    path('traits/<int:pk>/update/', views.TraitUpdate.as_view(), name='traits_update'),
    path('traits/<int:pk>/delete/', views.TraitDelete.as_view(), name='traits_delete'), 
    path('accounts/signup', views.signup, name='signup'), 
] 