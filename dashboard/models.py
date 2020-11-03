from django.db import models
from users.models import *
# Create your models here.

class Dashboard(models.Model):
    name = models.CharField(max_length=255, default='no name')
    user = models.ForeignKey(UserP, on_delete=models.CASCADE)

class Date(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    dashboard =  models.ForeignKey(Dashboard, on_delete=models.CASCADE)




# для виджета продолжительность работы
class DurationIntervalDay(models.Model):
    start = models.TimeField('start work')
    end = models.TimeField('end work')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)





# для виджета остатки на складах
class RemainderStorehouse(models.Model):
    name = models.CharField(max_length=255, default='no name')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

class RemainderIso(models.Model):
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)

class RemainderPol(models.Model):
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)

class RemainderPen(models.Model):
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)



# для виджета Выпуск панелей
class EditionDay(models.Model):
    suitable = models.FloatField()
    substandard = models.FloatField()
    defect = models.FloatField()
    flooded = models.FloatField()
    sum = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)


# для виджета Суммарный расход
class SumexpenseDay(models.Model):
    iso = models.FloatField()
    pol = models.FloatField()
    pen = models.FloatField()
    kat1 = models.FloatField()
    kat2 = models.FloatField()
    kat3 = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)




# для виджета Расход энергоресурсов
class EnergyConsumptionDay(models.Model):
    input1 = models.FloatField()
    input2 = models.FloatField()
    gas = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)





# для виджета Удельный расход на км
class SpecificConsumptionDay(models.Model):
    iso = models.FloatField()
    pol = models.FloatField()
    pen = models.FloatField()
    kat1 = models.FloatField()
    kat2 = models.FloatField()
    kat3 = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

