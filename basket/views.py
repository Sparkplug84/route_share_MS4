from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_basket(request):
    """ A view to return the basket contents """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view to add a membership type to the basket """

    membership_qty = 1
    basket = request.session.get('basket', {})

    if request.user.is_authenticated:
        if basket.items():
            messages.error(request, (
                "You've already added a Membership Plan to your basket."))
            return redirect('view_basket')

        basket[item_id] = basket.get(item_id, membership_qty)
        request.session['basket'] = basket

        messages.success(request, (
            "You've added a Membership Plan to your basket!"))
        return redirect(reverse('membership'))

    messages.error(request, (
        "You need to be signed in to add a Membership Plan to the basket."))
    return redirect('account_signup')


def empty_basket(request):
    """ A view to empty the basket """

    basket = request.session.get('basket')
    basket.clear()
    request.session['basket'] = basket
    messages.success(request, 'Your shopping basket is now empty.')
    return redirect(reverse('view_basket'))
