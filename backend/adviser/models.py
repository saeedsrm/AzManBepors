from django.db import models
from accounts.models import CustomUser, Responder
from django_jalali.db import models as jmodels
from jalali_date import datetime2jalali, date2jalali


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    name = models.CharField(max_length=20, unique=True, verbose_name="نام دسته بندی")
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='scategory',
                                     verbose_name="زیر دسته بندی")
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = "برچسب سوال"
        verbose_name_plural = "برچسب سوالات"

    name = models.CharField(max_length=20, unique=True, verbose_name="نام")

    def __str__(self):
        return self.name


class CreateNewQuestion(models.Model):
    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = " سوالات"

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE,
                                 verbose_name="دسته بندی سوال")
    tag = models.ForeignKey(Tag, related_name="tag", on_delete=models.CASCADE, verbose_name="تگ سوال")
    question = models.TextField(verbose_name="سوال")
    data_create = jmodels.jDateField(auto_now=True, verbose_name="تاریخ ایجاد سوال")
    is_public = models.BooleanField(default=True)
    STATUS = (
        ("answered", "has been answered"),
        ("waiting", "Waiting for members' response"),
        ("following", "Following up from the relevant official"),
        ("closed", "Closed"),
        ("open", "Open")
    )
    status = models.CharField(max_length=20, choices=STATUS, verbose_name="وضعیت پاسخ گویی")

    def get_jalali_date(self):
        return datetime2jalali(self.data_create)

    def __str__(self):
        return self.question


class Answer(models.Model):
    class Meta:
        verbose_name = "پاسخ سوال"
        verbose_name_plural = "پاسخ سوالات"

    author = models.ForeignKey(Responder, on_delete=models.CASCADE, verbose_name="فرد پاسخگو")
    answer = models.TextField(verbose_name="پاسخ")
    date_time = jmodels.jDateField(auto_now=True, verbose_name="تاریخ پاسخ به سوال")
    question = models.ForeignKey(CreateNewQuestion, related_name="answers", on_delete=models.CASCADE,
                                 verbose_name="پاسخ سوال")

    def get_jalali_date(self):
        return datetime2jalali(self.date_time)
