from django.utils import timezone

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name_plural = 'Categories'

        def __str__(self):
            return self.name


class Expense(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name_plural = 'Expenses'

        def __str__(self):
            return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

