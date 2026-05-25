from django.shortcuts import render, get_object_or_404
from .models import SamplingLocation, SoilSample, RadionuclideMeasurement
def index(request):
    num_samples = SoilSample.objects.count()
    num_measurements = RadionuclideMeasurement.objects.count()
    num_locations = SamplingLocation.objects.count()
    return render(request, 'radionuclides/index.html', {
        'num_samples': num_samples,
        'num_measurements': num_measurements,
        'num_locations': num_locations,
    })

def location_list(request):
    locations = SamplingLocation.objects.all()
    return render(request, 'radionuclides/location_list.html', {'locations': locations})

def location_detail(request, pk):
    location = get_object_or_404(SamplingLocation, pk=pk)
    samples = SoilSample.objects.filter(location=location).order_by('year')
    return render(request, 'radionuclides/location_detail.html', {
        'location': location,
        'samples': samples,
    })