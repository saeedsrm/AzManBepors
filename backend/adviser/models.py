from django.db import models
from accounts.models import CustomUser, Responder


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    name = models.CharField(max_length=20, unique=True,verbose_name="نام دسته بندی")
    sub_category = models.CharField(max_length=20,verbose_name="زیر دسته بندی")
    is_sub = models.BooleanField(default=False)


class Tag(models.Model):
    class Meta:
        verbose_name = "برچسب سوال"
        verbose_name_plural = "برچسب سوالات"
    name = models.CharField(max_length=20, unique=True,verbose_name="نام")


class Answer(models.Model):
    class Meta:
        verbose_name = "پاسخ سوال"
        verbose_name_plural = "پاسخ سوالات"
    author = models.ForeignKey(Responder, on_delete=models.CASCADE,verbose_name="فرد پاسخگو")
    answer = models.TextField(verbose_name="پاسخ")
    date_time = models.DateTimeField(auto_now=True)


class CreateNewQuestion(models.Model):
    class Meta:
        verbose_name = "ایجاد سوال جدید"
        verbose_name_plural = "ایجاد سوالات جدید"
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='کاربر')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="دسته بندی سوال")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,verbose_name="تگ سوال")
    question = models.TextField(verbose_name="سوال")
    data_create = models.DateField(auto_now=True)
    is_public = models.BooleanField(default=True)
    STATUS = (
        ("answered", "has been answered"),
        ("waiting", "Waiting for members' response"),
        ("following", "Following up from the relevant official"),
        ("closed", "Closed"),
        ("open", "Open")
    )
    status = models.CharField(max_length=20, choices=STATUS,verbose_name="وضعیت پاسخ گویی")
