# Generated by Django 4.2.1 on 2023-06-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0007_genre_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/genre/real-friends.jpg', upload_to='uploads/genre/', verbose_name='picture name'),
        ),
    ]
