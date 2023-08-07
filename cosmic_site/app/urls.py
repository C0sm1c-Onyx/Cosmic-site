from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('asteroids/', asteroid_page),
    path('planets/', planet_page),
    path('stars/', star_page),
    path('nebulae/', nebula_page),
    path('galaxies/', galaxy_page),
    path('black_holes/', black_hole_page),
    path('space_time/', space_time_page),
    path('dark_energy/', dark_energy_page),
    path('universe/', universe_page),
    path('interesing-facts/', interesing_facts_page, name='facts'),
    path('additional_information/', info_page, name='info'),
    path('contacts/', contacts_page, name='contacts'),
    path('add_fact/', add_fact, name='add_fact'),
    path('/', sign_in, name='sign_in')
]
