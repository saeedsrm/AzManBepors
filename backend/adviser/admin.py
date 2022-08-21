from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('answer',
                    'get_username', 'get_date_time', 'answer')
    list_display_links = ('answer', 'get_username', 'get_date_time',
                          )

    def get_username(self, obj):
        return obj.author.user.username

    get_username.short_description = 'نام کاربری پاسخ دهنده'

    def get_date_time(self, obj):
        return obj.date_time

    get_date_time.short_description = 'تاریخ پاسخ'


class QusetionAdmin(admin.ModelAdmin):
    model = CreateNewQuestion
    list_display = (
        'tag', 'category', 'data_create', 'get_username', 'status','pk')

    list_display_links = ('tag', 'category', 'data_create', 'get_username', 'status','pk'
                          )

    def get_username(self, obj):
        return obj.author.username

    get_username.short_description = 'نام کاربری'


admin.site.register(CreateNewQuestion, QusetionAdmin)
admin.site.register(Answer, AnswerAdmin)
