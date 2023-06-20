# Generated by Django 4.2.1 on 2023-06-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_book_activ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='activ',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.BigIntegerField(blank=True, default=2023, verbose_name='Year book'),
        ),
    ]
