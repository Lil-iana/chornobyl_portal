import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chornobyl_site.settings')
django.setup()

from radionuclides.models import LandscapeType, SamplingLocation, SoilSample, RadionuclideMeasurement

# Очищаємо старі дані
RadionuclideMeasurement.objects.all().delete()
SoilSample.objects.all().delete()
SamplingLocation.objects.all().delete()
LandscapeType.objects.all().delete()

# 2 типи ландшафтів
l1 = LandscapeType.objects.create(name='Вододільні рівнини', slug='vododilni', description='Автономні вододільні рівнини')
l2 = LandscapeType.objects.create(name='Заплавні тераси', slug='zaplavni', description='Акумулятивні заплави')

# 2 точки відбору
p1 = SamplingLocation.objects.create(name='Точка 1 — Рудий ліс', landscape_type=l1, latitude=51.389, longitude=30.099)
p2 = SamplingLocation.objects.create(name="Точка 2 — Заплава Прип'яті", landscape_type=l2, latitude=51.400, longitude=30.120)

# Проби — 3 роки для кожної точки
s1_1999 = SoilSample.objects.create(location=p1, year=1999, depth_cm=10, collected_by='Мазурик Л.')
s1_2009 = SoilSample.objects.create(location=p1, year=2009, depth_cm=10, collected_by='Мазурик Л.')
s1_2023 = SoilSample.objects.create(location=p1, year=2023, depth_cm=10, collected_by='Мазурик Л.')
s2_1999 = SoilSample.objects.create(location=p2, year=1999, depth_cm=20, collected_by='Мазурик Л.')
s2_2009 = SoilSample.objects.create(location=p2, year=2009, depth_cm=20, collected_by='Мазурик Л.')
s2_2023 = SoilSample.objects.create(location=p2, year=2023, depth_cm=20, collected_by='Мазурик Л.')

# Вимірювання
data = [
    (s1_1999, 'Cs137', 450000, 15000), (s1_1999, 'Sr90', 12000, 800),
    (s1_1999, 'Am241', 980, 60), (s1_2009, 'Cs137', 380000, 12000),
    (s1_2009, 'Sr90', 9500, 600), (s1_2009, 'Am241', 1850, 90),
    (s1_2023, 'Cs137', 210000, 8000), (s1_2023, 'Sr90', 6800, 400),
    (s1_2023, 'Am241', 1200, 75), (s2_1999, 'Cs137', 680000, 22000),
    (s2_1999, 'Sr90', 18000, 1100), (s2_1999, 'Am241', 750, 45),
    (s2_2009, 'Cs137', 520000, 18000), (s2_2009, 'Sr90', 14000, 900),
    (s2_2009, 'Am241', 1420, 85), (s2_2023, 'Cs137', 390000, 13000),
    (s2_2023, 'Sr90', 9800, 580), (s2_2023, 'Am241', 980, 58),
]

for sample, nuclide, conc, unc in data:
    RadionuclideMeasurement.objects.create(sample=sample, radionuclide=nuclide, concentration=conc, uncertainty=unc)

print('Готово! Дані додано успішно.')