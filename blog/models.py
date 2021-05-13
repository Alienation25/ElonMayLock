from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    button_url=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#Перегрузка функция для  преобразование объекта к строковому представлению, вызывается, когда объект передается функциям print() и str()
        return self.title



class docsP(models.Model):
    image = models.ImageField(null=True, blank=True)
    