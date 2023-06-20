# Generated by Django 4.2.1 on 2023-06-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0008_alter_genre_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Book name')),
                ('picture', models.ImageField(blank=True, default='uploads/genre/real-friends.jpg', upload_to='uploads/genre/', verbose_name='picture book')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='reference.genre', verbose_name='Genre')),
            ],
        ),
    ]
