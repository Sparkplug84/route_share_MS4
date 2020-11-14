from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

# MinValueValidator found on stack overflow to give length field a min value.
from django.core.validators import MinValueValidator


class BikeType(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class RouteType(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Route(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    bike_type = models.ForeignKey(
        'BikeType', null=False, blank=False, on_delete=models.CASCADE)
    length = models.DecimalField(
        max_digits=4, decimal_places=1, validators=[MinValueValidator(5)])
    route_type = models.ForeignKey(
        'RouteType', null=False, blank=False, on_delete=models.CASCADE)
    map_url = models.URLField(max_length=1054)
    country = CountryField(blank_label='Country *')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
