from django.contrib import admin
from .models import LandscapeType, SamplingLocation, SoilSample, RadionuclideMeasurement

admin.site.register(LandscapeType)
admin.site.register(SamplingLocation)
admin.site.register(SoilSample)
admin.site.register(RadionuclideMeasurement)
