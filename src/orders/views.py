from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, FormView, TemplateView, UpdateView
from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404
from books.models import Book
from .models import Cart, BookInCart, Order
from reference.models import Status
from django.db import models
from . import forms
from person.models import Person

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
        good_id = self.request.GET.get("good")
        action = self.request.GET.get("action")
        if good_id and action and action in ['add', 'delete']:
            good = Book.objects.get(pk=int(good_id))
            price = Book.objects.get(pk=int(good_id)).price
            good_in_cart = get_object_or_404(
                BookInCart,
                cart__pk=cart.pk,
                good__pk=good.pk,
            )
            if action == "add":
                addition = 1
            else:
                if good_in_cart.quantity <= 1:
                    good_in_cart.delete()
                    return cart
                addition = -1
            good_in_cart.quantity = good_in_cart.quantity + addition
            good_in_cart.price = good_in_cart.quantity * price
            good_in_cart.save()
        return cart


class OrderCreateView(FormView):
    form_class = forms.CreateOrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy("orders:order-complite")

    def form_valid(self, form):
        delivery_adress = form.cleaned_data.get('delivery_adress')
        status = Status.objects.get(pk=4)
        
        cart_pk = self.request.session.get("cart_id")
        # updating the USER when forming an order 
        customer_login = Cart.objects.get(pk=cart_pk)
        customer_login.customer=self.request.user
        customer_login.save(update_fields=["customer"])
        #
        cart = get_object_or_404(
           Cart, 
           pk=cart_pk,
        
        ) 
        obj = Order.objects.create(
            delivery_adress = delivery_adress,
            status= status,
            cart= cart
        )
      
        del self.request.session['cart_id']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get('cart_id')
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
            cont["object"] = Cart.objects.get(pk=cart_pk)
            
        return cont
    
class OrderSuccess(TemplateView):
    template_name = "orders/order_complite.html"

#Update   
class OrderUpdateView(UpdateView):
    model= Order
    form_class= forms.OrderModelForm
    template_name = "orders/order_update.html"
    success_url= '/'
    # success_url= '/person/user-list'
    # установил саксес урл на главную страницу т.к. покупателю на юзерлист нельзя . Надо подумать как переопределить урл     

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["object_cart"] = BookInCart.objects.all()
        return cont

#Detail    
class OrderDetailView(DetailView):
    model= Order
    template_name = 'orders/order_detail.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["object_cart"] = BookInCart.objects.all()
        return cont