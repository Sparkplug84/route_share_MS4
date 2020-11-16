from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order
from profiles.models import UserProfile

import time


class StripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the user a confirmation email """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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

        # update profile information if save_info checked
        username = intent.metadata.username
        profile = UserProfile.objects.get(user__username=username)
        if save_info:
            profile.default_full_name = billing_details.name
            profile.default_email = billing_details.email
            profile.default_street_address1 = billing_details.address.line1
            profile.default_street_address2 = billing_details.address.line2
            profile.default_town_or_city = billing_details.address.city
            profile.default_country = billing_details.address.country
            profile.save()

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
                    country__iexact=billing_details.address.country,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            print(f"ORDER (does exist) - WEBHOOK: {order}")
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database.', status=200)
        else:
            order = None
            try:
                # for item_id, quantity in json.loads(basket).items():
                #     membership = get_object_or_404(Membership, pk=item_id)
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    street_address1=billing_details.line1,
                    street_address2=billing_details.line2,
                    town_or_city=billing_details.city,
                    country=billing_details.address.country,
                    membership=membership,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order.save()
                print(f"ORDER (doesn't exist) - WEBHOOK: {order}")
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} \
                             | ERROR: {e}', status=500)

        # self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
