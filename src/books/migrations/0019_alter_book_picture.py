# Generated by Django 4.2.1 on 2023-07-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_alter_book_pages_alter_book_ves_alter_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/genre/image.png', upload_to='uploads/genre/', verbose_name='picture book'),
        ),
    ]