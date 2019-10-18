from django.db import models

class Address(models.Model):
    country = models.CharField(verbose_name='country', max_length=20)
    city = models.CharField(verbose_name='city', max_length=20)
    street = models.CharField(verbose_name='street', max_length=30)
    number = models.IntegerField(verbose_name='house number')
    code = models.CharField(verbose_name='code', max_length=7)

    def __str__(self):
        return self.street + self.number
