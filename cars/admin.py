from django.contrib import admin
from cars.models import (
    Car, Generation, BodyType, Engine, AvailableEngine, CarStats, Transmission,
)

models = (
    Car, Generation, BodyType, Engine, AvailableEngine, CarStats, Transmission,
)
for model in models:
    admin.site.register(model)
