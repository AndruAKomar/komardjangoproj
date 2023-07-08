from django.db import models
from django.conf import settings

# Create your models here.

#расcширяем поля для ЮЗЕРА
# class Person(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,)
#     telephone_number = models.CharField(
#         verbose_name='Telephone number',
#         max_length=20,
#         blank=True,
#         null=True)
#     home_address=models.CharField(
#         verbose_name='Home address',
#         max_length=50,
#         blank=True,
#         null=True)
#     delivery_adress=models.CharField(
#         verbose_name='Delivery adress',
#         max_length=50,
#         blank=True,
#         null=True)
#     description = models.TextField(
#         verbose_name='Other information',
#         null=True,
#         blank=True)
    
#     def __str__(self):
#         return 'Person for user {}'.format(self.user.username)