from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect('membership')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HMevpF3StHkhbsY4dtTWM8bedI1tpFheIP2FN3D38ehS5rC7wvog4c0O4DJMgqSMCRdWE3mq7fTEyftw72xaCBC007LMNc8uN',
        'client_secret': 'test client key',
    }

    return render(request, template, context)
