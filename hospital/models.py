from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyAccountManager

class Address(models.Model):
    country     = models.CharField(verbose_name='country', max_length=20)
    city        = models.CharField(verbose_name='city', max_length=20)
    street      = models.CharField(verbose_name='street', max_length=30)
    number      = models.IntegerField(verbose_name='house number')
    code        = models.CharField(verbose_name='code', max_length=7)

class Account(AbstractBaseUser):
    GENDER = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    first_name          = models.CharField(verbose_name='first name',max_length=50)
    last_name           = models.CharField(verbose_name='last name',max_length=50)
    date_of_birth       = models.DateField(verbose_name='date of birth')
    phone_number        = models.CharField(verbose_name='phone number',max_length=40, unique=True)
    gender              = models.CharField(verbose_name='gender', max_length=1, choices=GENDER)
    address             = models.OneToOneField(Address, on_delete=models.CASCADE, parent_link=True, null=True, blank=True)
    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS     = ['username', 'first_name',]
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
        
    def has_module_perms(self, app_label):
        return True
