from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Order
from membership.models import Membership

import json
import time


class StripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic, unknown or unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        membership = intent.metadata.membership

        billing_details = intent.charges.data[0].billing_details

        # Clean the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city__iexact=billing_details.address.city,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database.', status=200)
        else:
            order = None
            try:
                for item_id, quantity in json.loads(basket).items():
                    membership = get_object_or_404(Membership, pk=item_id)
                    order = Order.objects.create(
                        full_name=billing_details.name,
                        email=billing_details.email,
                        street_address1=billing_details.line1,
                        street_address2=billing_details.line2,
                        town_or_city=billing_details.city,
                        membership=membership,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    order.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} \
                             | ERROR: {e}', status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
