from django.shortcuts import render, redirect
from .models import *

from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    items = Item.objects.all()
    if items:
        return render(request, 'home.html', {'items': items})
    return render(request, 'home.html', {})


def buy_item(request, id):
    item = Item.objects.get(id=id)
    session = None
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/',
        )

        return redirect(session.url, code=303)
    return render(request, 'buy_item.html', {'session': session})


def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'get_item.html', {'item': item})


def success(request):
    return render(request, 'success.html', {})
