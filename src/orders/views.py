from django.shortcuts import render
from django.views.generic import DetailView
from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404
from books.models import Book
from .models import Cart, BookInCart
from reference.models import Status
from django.db import models

# Create your views here.

class CartDetailView(DetailView):
    template_name="orders/cart.html"
    model=Cart

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get("cart_id")
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
        return cont

    def get_object(self, *args, **kwargs):
        # cart_id
        cart_pk = self.request.session.get("cart_id") # int / None
        customer = self.request.user # User / AnonimousUser -> User / None
        if customer.is_anonymous:
            customer = None
        cart, created = Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        # cart
        good_id = self.request.GET.get("good_id")
        quantity = self.request.GET.get("quantity")
        if good_id and quantity:
            quantity = int(quantity)
            good = Book.objects.get(pk=int(good_id))
            price = Book.objects.get(pk=int(good_id)).price
            good_in_cart, good_in_cart_created = BookInCart.objects.get_or_create(
                cart=cart,
                good=good,
                defaults={
                    "quantity":quantity,
                    "price": price * quantity
                }
            )
            if not good_in_cart_created:
                good_in_cart.quantity = good_in_cart.quantity + quantity
                good_in_cart.price = good_in_cart.price + price*quantity
                good_in_cart.save()
            if created:
                self.request.session['cart_id'] = cart.pk
        return cart


class CartAddDeleteItemView(DetailView):
    template_name = "orders/cart.html"
    model = Cart
    def get_object(self, *args, **kwargs):
        # cart_id
        cart_pk = self.request.session.get("cart_id") # int / None
        customer = self.request.user # User / AnonimousUser -> User / None
        if customer.is_anonymous:
            customer = None
        cart, created = Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        # cart
        good_id = self.request.GET.get("good")
        action = self.request.GET.get("action")
        if good_id and action and action in ['add', 'delete']:
            good = Book.objects.get(pk=int(good_id))
            price = Book.objects.get(pk=int(good_id)).price
            print(cart, good)
            good_in_cart = get_object_or_404(
                BookInCart,
                cart__pk=cart.pk,
                good__pk=good.pk,
            )
            if action == "add":
                addition = 1
            else:
                addition = -1
            good_in_cart.quantity = good_in_cart.quantity + addition
            good_in_cart.price = good_in_cart.quantity * price
            good_in_cart.save()
        return cart




# <script>
#       function addGood(pk) {
#         console.log("add" + pk)
#         redirect("add", pk)
#       }
#       function deleteGood(pk) {
#         console.log("delete" + pk)
#         redirect("delete", pk)
#       }
#       function redirect(action, pk) {
#         window.location.href = "{% url "orders:cart-items-edit" %}" + '?action=${action}&good=' + pk;
#       }
#   </script>