# Generated by Django 4.2.1 on 2023-06-26 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0018_alter_book_pages_alter_book_ves_alter_book_year'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='orders.cart', verbose_name='Cart')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Book')),
            ],
        ),
    ]
