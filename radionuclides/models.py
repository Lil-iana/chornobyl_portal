from django.db import models

NUCLIDE_CHOICES = [
    ('Cs137', 'Cs-137'),
    ('Sr90', 'Sr-90'),
    ('Pu238', 'Pu-238'),
    ('Pu239_240', 'Pu-239+240'),
    ('Am241', 'Am-241'),
]

YEAR_CHOICES = [(1999, '1999'), (2009, '2009'), (2023, '2023')]


class LandscapeType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SamplingLocation(models.Model):
    name = models.CharField(max_length=200)
    landscape_type = models.ForeignKey(LandscapeType, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SoilSample(models.Model):
    location = models.ForeignKey(SamplingLocation, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES)
    depth_cm = models.FloatField(null=True, blank=True)
    collected_by = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.location} — {self.year}"


class RadionuclideMeasurement(models.Model):
    sample = models.ForeignKey(SoilSample, on_delete=models.CASCADE, related_name='measurements')
    radionuclide = models.CharField(max_length=20, choices=NUCLIDE_CHOICES)
    concentration = models.FloatField(help_text="Бк/кг")
    uncertainty = models.FloatField(null=True, blank=True, help_text="±")

    def __str__(self):
        return f"{self.radionuclide}: {self.concentration} Бк/кг"
