from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from jalali_date import datetime2jalali, date2jalali


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'

    fullname = models.CharField(max_length=30, verbose_name="نام و نام خانوادگی", null=True, blank=True)
    first_name = models.CharField(max_length=60, verbose_name='نام', null=True, blank=True)
    username = models.CharField(max_length=40, verbose_name="نام کاربری", null=True, blank=True)
    last_name = models.CharField(max_length=60, verbose_name='نام خانوادگی', null=True, blank=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    collage = models.CharField(max_length=20, verbose_name="دانشکده", null=True, blank=True)
    major = models.CharField(max_length=20, verbose_name="رشته تحصیلی", null=True, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    entering_year = models.CharField(max_length=8, verbose_name="سال ورود", null=True, blank=True)
    phone_number = models.CharField(max_length=30, verbose_name="تلفن همراه", unique=True, null=True, blank=True)
    student_code = models.CharField(max_length=13, null=True, blank=True, unique=True)
    is_staff = models.BooleanField(default=False, verbose_name="آیا مدیر است؟")
    is_active = models.BooleanField(default=True, verbose_name='آیا فعال است؟')
    score = models.IntegerField(default=0, null=True, blank=True, verbose_name="امتیاز")
    date_joined = jmodels.jDateField(auto_now_add=True, verbose_name="تاریخ عضویت")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_jalali_date(self):
        return datetime2jalali(self.date_joined)

    def __str__(self):
        return self.phone_number


class Responder(models.Model):
    class Meta:
        verbose_name = 'کاربر راهنما'
        verbose_name_plural = 'کاربران راهنما'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="کاربر")
    fields_of_activity = models.TextField(verbose_name="زمینه های فعالیت")
    interests = models.TextField(verbose_name="علاقه مندی ها")
    descriptions = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return f'{self.user.phone_number}'
