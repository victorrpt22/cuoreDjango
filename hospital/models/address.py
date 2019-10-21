from django.db import models

class Address(models.Model):
    COUNTRIES = (
        ('mx', 'Mexico'),
        ('us', 'Unites States'),
        ('ca', 'Canada')
    )
    country = models.CharField(verbose_name='country', max_length=20, choices=COUNTRIES)
    city = models.CharField(verbose_name='city', max_length=20)
    street = models.CharField(verbose_name='street', max_length=30)
    number = models.CharField(verbose_name='house number', max_length=30)
    code = models.CharField(verbose_name='code', max_length=7)

    def __str__(self):
        return self.street + self.number
