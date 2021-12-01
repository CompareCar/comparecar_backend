from django.contrib import admin
from cars.models import (
    Car, Generation, BodyType, Engine, CarStats, Transmission,
)

models = (Car, Generation, BodyType, Engine, CarStats, Transmission)
for model in models:
    admin.site.register(model)
