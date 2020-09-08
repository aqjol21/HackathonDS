from django.db import models

# Create your models here.
class Route(models.Model):
    source = models.CharField("Откуда", max_length=64)
    departure = models.DateField("Departure")
    destination = models.CharField("Куда", max_length=64)
    # arrival = models.DateTimeField("Arrival")
    price = models.IntegerField("Cтоимость")
    company = models.CharField("Компания", max_length=64)
    isBusiness = models.BooleanField("Класс", default=False)
    isPlane = models.BooleanField("Самолет", default=True)
    isTrain = models.BooleanField("Поезд", default=False)
    isBus = models.BooleanField("Автобус", default=False)
    duration = models.IntegerField("Длительность")
    distance = models.IntegerField("Дистанция")

    def __str__(self):
        return self.source + "-" + self.destination
