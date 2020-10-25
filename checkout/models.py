import uuid
from django.db import models
from django.contrib.auth.models import User
from membership.models import Membership


class Order(models.Model):
    """ Model to define all the fields required to save an order """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _generate_order_number(self):
        """ Generate a unique random order number """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override the original save order method
        to set the order numer if it hasn't been set yet """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save()

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    membership = models.ForeignKey(
        Membership, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.quantity} {self.membership.name} ' \
            'on order {order.order_number}'
