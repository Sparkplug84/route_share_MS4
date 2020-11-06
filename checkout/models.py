import uuid
from django.db import models
from membership.models import Membership
from django_countries.fields import CountryField


class Order(models.Model):
    """ Model to define all the fields required to save an order """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    membership = models.ForeignKey(
        Membership, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1, editable=False)
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generate a unique random order number """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Overrides the original save method to set the the order total """
        self.order_total = self.membership.price
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
