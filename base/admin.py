from django.contrib import admin

from base.models import Expense, Subscriber


# Register your models here.


class AdminSubscriber(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ['name']


admin.site.register(Subscriber, AdminSubscriber)
