# Generated by Django 4.2.1 on 2023-06-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_formatbook_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='agerestrict',
            field=models.CharField(blank=True, max_length=30, verbose_name='Age restrictions book'),
        ),
        migrations.AddField(
            model_name='book',
            name='ves',
            field=models.BigIntegerField(blank=True, default=1, verbose_name='ves book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.BigIntegerField(blank=True, verbose_name='ISBN book'),
        ),
    ]
