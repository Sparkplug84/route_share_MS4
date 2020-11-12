from django.db import models

from django_countries.fields import CountryField


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
        'BikeType', null=True, blank=True, on_delete=models.SET_NULL)
    length = models.DecimalField(max_digits=4, decimal_places=1)
    route_type = models.ForeignKey(
        'RouteType', null=True, blank=True, on_delete=models.SET_NULL)
    map_url = models.URLField(max_length=1054)
    country = CountryField(blank_label='Country *')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
