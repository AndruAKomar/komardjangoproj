# Generated by Django 4.2.1 on 2023-06-20 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_dateadd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='dateadd',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date add'),
        ),
    ]
