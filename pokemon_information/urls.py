from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('external/<str:pokemon_name>/', views.save_pokemon, name='save_pokemon'),
    path('details/<int:id>/', views.get_pokemon_details, name='get_pokemon_details'),
    path('update/<int:id>/', views.update_pokemon_details, name='update_pokemon_details')
]
