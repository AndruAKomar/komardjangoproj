from typing import Any, Dict
from django.views import generic
from books import models
from books.models import Book
from django.contrib.auth.models import Group
from orders.models import Cart, BookInCart
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect



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
        # del self.request.session['cart_id']
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get("cart_id")
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
        else: cont["total_quantity_in_cart"] =0   
        return cont
    
    