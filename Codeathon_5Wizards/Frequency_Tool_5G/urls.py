from django.contrib import admin
from django.urls import path
from . import Frequency_Tool_Views


urlpatterns = [
    path('', Frequency_Tool_Views.freq_homepage, name = "Homepage"),
    path('freq_calculation', Frequency_Tool_Views.freq_calculation, name="freq_calculation"),
]

