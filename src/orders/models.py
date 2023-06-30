from django.db import models
from django.contrib.auth  import get_user_model
from books.models import Book
from reference.models import Status
# Create your models here.
User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name='Customer',
        on_delete=models.PROTECT,
        related_name='carts',
        null=True,
        blank=True 
    )
    @property
    def total_price(self):
        total_price=0
        for good_in_cart in self.books.all():
            total_price += good_in_cart.price
        return total_price
    @property
    def total_quantity(self):
        total_quantity=0
        for good_in_cart in self.books.all():
            total_quantity += good_in_cart.quantity
        return total_quantity

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        on_delete=models.CASCADE, 
        related_name='books'
    )
    good =models.ForeignKey(
        Book,
        verbose_name='Book', 
        on_delete=models.PROTECT
        )
    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=1
        )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=6,
        decimal_places=2
        )
    created = models.DateTimeField(
        verbose_name='Created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self) -> str:
        return f'{self.good.name} x {self.quantity}'
    
class Order(models.Model):
    delivery_adress = models.TextField(
        verbose_name='Delivery_adress',
        default='Lenina' # add from adress          
    )
    cart = models.OneToOneField(
        Cart,
        verbose_name='Cart',
        on_delete=models.PROTECT
    )
    status = models.ForeignKey(
        Status,
        verbose_name='Status',
        on_delete=models.PROTECT,
        related_name='statuses',
        default=1
        )
    created = models.DateTimeField(
        verbose_name='Created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True,
        auto_now_add=False
    )