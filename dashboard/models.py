from django.db import models
from users.models import *
# Create your models here.





class Dashboard(models.Model):
    '''
    Сущность для определения виджетов

      Attributes
    ===========
    - name - str - название для записи

     Methods
    =============
    - None
    '''
    name = models.CharField(max_length=255, default='no name')

    def __str__(self):
        return self.name

class Role(models.Model):
    '''
        Сущность для определения роли пользователя

          Attributes
        ===========
        - name - str - название для записи
        - user - MtM - связь с сущностью UserP
        - dashboard - MtM - связь с сущностью Dashboard

         Methods
        =============
        - None
    '''
    name = models.CharField(max_length=255, default='no name')
    user = models.ManyToManyField(UserP)
    dashboard = models.ManyToManyField(Dashboard)


# class Date(models.Model):
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)




# для виджета продолжительность работы
class DurationIntervalDay(models.Model):
    '''
        Сущность для определения начало и времени работы

          Attributes
        ===========
        - start - Time - начало работы
        - end - Time - конец работы
        - date - Date - дата работы

         Methods
        =============
        - None
    '''
    start = models.TimeField('start work')
    end = models.TimeField('end work')
    date = models.DateField(auto_now=False, auto_now_add=False)





# для виджета остатки на складах
class RemainderStorehouse(models.Model):
    '''
        Сущность для определения остатков на складе

          Attributes
        ===========
        - name - str - название цеха
        - date - Date -  дата

         Methods
        =============
        - None
    '''
    name = models.CharField(max_length=255, default='no name')
    date = models.DateField(auto_now=False, auto_now_add=False)

class RemainderIso(models.Model):
    '''
        Сущность для определения остатков изоционата

          Attributes
        ===========
        - quantity - float - количество изоционата
        - storehouse - FK - внешний ключ для связи с сущностью  RemainderStorehouse

         Methods
        =============
        - None
    '''
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)

class RemainderPol(models.Model):
    '''
        Сущность для определения остатков полиола

          Attributes
        ===========
        - quantity - float - количество полиола
        - storehouse - FK - внешний ключ для связи с сущностью  RemainderStorehouse

         Methods
        =============
        - None
    '''
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)

class RemainderPen(models.Model):
    '''
        Сущность для определения остатков пентана

          Attributes
        ===========
        - quantity - float - количество пентана
        - storehouse - FK - внешний ключ для связи с сущностью  RemainderStorehouse

         Methods
        =============
        - None
    '''
    quantity = models.FloatField()
    storehouse = models.ForeignKey(RemainderStorehouse, on_delete=models.CASCADE)



# для виджета Выпуск панелей
class EditionDay(models.Model):
    '''
        Сущность для определения выпуска

          Attributes
        ===========
        - suitable - float -
        - substandard - float -
        - defect - float -
        - flooded - float -
        - sum - float -
        - date - Date -

         Methods
        =============
        - None
    '''
    suitable = models.FloatField()
    substandard = models.FloatField()
    defect = models.FloatField()
    flooded = models.FloatField()
    sum = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)


# для виджета Суммарный расход
class SumexpenseDay(models.Model):
    '''
        Сущность для определения сумарного расхода

          Attributes
        ===========
        - iso - float -
        - pol - float -
        - pen - float -
        - kat1 - float -
        - kat2 - float -
        - kat3 - float -
        - date - Date -

         Methods
        =============
        - None
    '''
    iso = models.FloatField()
    pol = models.FloatField()
    pen = models.FloatField()
    kat1 = models.FloatField()
    kat2 = models.FloatField()
    kat3 = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)




# для виджета Расход энергоресурсов
class EnergyConsumptionDay(models.Model):
    '''
        Сущность для определения сумарного расхода

          Attributes
        ===========
        - input1 - float -
        - input2 - float -
        - gas - float -
        - date - Date -

         Methods
        =============
        - None
    '''
    input1 = models.FloatField()
    input2 = models.FloatField()
    gas = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)





# для виджета Удельный расход на км
class SpecificConsumptionDay(models.Model):
    '''
        Сущность для определения удельного расхода

          Attributes
        ===========
        - iso - float -
        - pol - float -
        - pen - float -
        - kat1 - float -
        - kat2 - float -
        - kat3 - float -
        - date - Date -

         Methods
        =============
        - None
    '''
    iso = models.FloatField()
    pol = models.FloatField()
    pen = models.FloatField()
    kat1 = models.FloatField()
    kat2 = models.FloatField()
    kat3 = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)