from typing import cast

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=70)


class Generation(models.Model):
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE)
    generation = models.CharField(max_length=50)


class BodyType(models.Model):
    class TypeOfBody(models.TextChoices):
        SEDAN = 'Sedan'
        WAGON = 'Wagon'
        COUPE = 'Coupe'
        HATCHBACK = 'Hatchback'
        SUV = 'SUV'
        CONVERTIBLE = 'Convertible'
        PICKUP = 'Pickup'
        MINIVAN = 'Minivan'
        VAN = 'Van'

    body_type = models.CharField(choices=TypeOfBody.choices, max_length=50)
    generations = models.ManyToManyField(Generation)


class Engine(models.Model):
    class FuelType(models.TextChoices):
        PETROL = 'Petrol'
        DIESEL = 'Diesel'
        LPG = 'LPG'
        HYBRID = 'Hybrid'
        ELECTRIC = 'Electric'
        ETANOL = 'Etanol'
        HYDROGEN = 'Hydrogen'

    engine_capacity = models.PositiveSmallIntegerField()
    fuel_type = models.TextField(choices=FuelType.choices)
    cylinders = models.PositiveSmallIntegerField()
    power = models.PositiveSmallIntegerField()
    torque = models.PositiveSmallIntegerField()

    def __repr__(self):
        return (f'{round_engine_capacity(self.engine_capacity)} '
                f'{self.power}PS {self.fuel_type}')


class Transmission(models.Model):
    class TransmissionType(models.TextChoices):
        MANUAL = 'Manual'
        AUTOMATIC = 'Automatic'

    transmission_system = models.CharField(
        choices=TransmissionType.choices, max_length=50)
    number_of_gears = models.PositiveSmallIntegerField()


class CarStats(models.Model):
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    transmission = models.ForeignKey(
        Transmission, null=True, on_delete=models.CASCADE)
    # ---- general stats ----
    height = models.PositiveSmallIntegerField(
        help_text='Car height in cm', null=True, blank=True)
    width = models.PositiveSmallIntegerField(
        help_text='Car width in cm', null=True, blank=True)
    length = models.PositiveSmallIntegerField(
        help_text='Car length in cm', null=True, blank=True)
    num_of_seats = models.PositiveSmallIntegerField(null=True, blank=True)
    max_boot_capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    min_boot_capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    num_of_doors = models.PositiveSmallIntegerField(null=True, blank=True)
    turning_radius = models.PositiveSmallIntegerField(null=True, blank=True)
    year_of_start_production = models.PositiveSmallIntegerField(
        null=True, blank=True)
    year_of_end_production = models.PositiveSmallIntegerField(
        null=True, blank=True)
    fuel_tank_capacity = models.PositiveSmallIntegerField(
        null=True, blank=True)
    weight = models.PositiveSmallIntegerField(null=True, blank=True)
    # ---- performance stats ----
    v_max = models.PositiveSmallIntegerField(null=True, blank=True)
    acceleration_0_100 = models.FloatField(null=True, blank=True)
    acceleration_100_200 = models.FloatField(null=True, blank=True)
    time400 = models.FloatField(
        help_text='Time of 400 meters drag race', null=True,
        blank=True,
    )
    nurburgring_lap_time = models.PositiveSmallIntegerField(
        null=True, blank=True)


def round_engine_capacity(capacity: models.PositiveSmallIntegerField):
    """
    Rounds engine capacity in milliliters to  colloquial form.
    Examples:
    1998 -> 2.0
    1897 -> 1.9
    12011 -> 12.0
    798 -> 0.8
    """
    capacity = cast(int, capacity)
    rounded_capa = str(round(capacity / 100))
    capa_with_dot = f'{rounded_capa[:-1]}.{rounded_capa[-1]}'
    return capa_with_dot if capa_with_dot[0] != '.' else '0' + capa_with_dot

#from cars.models import Car, Generation, TypeOfBody, BodyType, Engine, CarStats, Transmission, TransmissionType
