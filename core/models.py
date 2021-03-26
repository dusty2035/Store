from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class CustomUserManager(BaseUserManager):


    def create_user(self, email, phone_number, password, **extra_fields):
        if not email :
            raise ValueError("user must provide an email")
        if not phone_number :
            raise ValueError("user most provie a phone_number")
        user = self.model(email=self.normalize_email(email), phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(email, phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number']