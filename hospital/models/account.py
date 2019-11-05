from django.db import models
from django.contrib.auth.models import AbstractUser
from hospital.managers import MyAccountManager

class Account(AbstractUser):
    GENDER = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    ROLE = (
        ('staff', 'Staff'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(verbose_name='role', max_length=12, choices=ROLE)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(verbose_name='date of birth', null=True, blank=True)
    phone_number = models.CharField(verbose_name='phone number',max_length=40, null=True, blank=True)
    username = models.CharField(verbose_name='username',max_length=40)
    gender = models.CharField(verbose_name='gender', max_length=1, choices=GENDER, null=True, blank=True)
    address = models.ForeignKey('Address', related_name='address', on_delete=models.SET_NULL, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
