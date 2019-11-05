from django.db import models

class Address(models.Model):
    COUNTRIES = (
        ('mx', 'Mexico'),
        ('us', 'Unites States'),
        ('ca', 'Canada')
    )
    country = models.CharField(verbose_name='country', max_length=20, choices=COUNTRIES, null=True, blank=True)
    city = models.CharField(verbose_name='city', max_length=20, null=True, blank=True)
    street = models.CharField(verbose_name='street', max_length=30,null=True, blank=True)
    number = models.CharField(verbose_name='house number', max_length=30,null=True, blank=True)
    code = models.CharField(verbose_name='code', max_length=7,null=True, blank=True)

    def __str__(self):
        return self.street + self.number
