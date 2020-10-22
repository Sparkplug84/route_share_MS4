from django.shortcuts import get_object_or_404
from membership.models import Membership


def basket_contents(request):

    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        membership = get_object_or_404(Membership, pk=item_id)
        total += quantity * membership.price
        basket_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'membership': membership,
            }
        )

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
