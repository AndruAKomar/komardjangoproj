# Generated by Django 4.2.1 on 2023-06-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0009_alter_series_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Order_status')),
            ],
        ),
    ]
