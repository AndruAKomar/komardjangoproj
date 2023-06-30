from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from books import models
from books.models import Book
from django.contrib.auth.models import Group
from orders.models import Cart



# Create your views here.

#HomePage 
# class HomePage(generic.TemplateView):
#     template_name='home/index.html'
#    
    
# ListView
class HomePage(generic.ListView):
    template_name='home/index.html'
    model= models.Book
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get("cart_id")
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=3).total_quantity
        return cont