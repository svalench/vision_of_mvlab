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

class TableName(models.Model):
    name = models.CharField(max_length=255, default='no name')
    dash = models.ForeignKey(Dashboard, models.SET_NULL, blank=True, null=True)

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
        - suitable - float - количество годного
        - substandard - float - количество некондиции
        - defect - float - количество брака
        - flooded - float - количество залитого
        - sum - float - сумма годного, некондиции, брака
        - date - Date - дата

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
        - iso - float - количество расхода изоцианата
        - pol - float - количество расхода полиола
        - pen - float - количество расхода пентана
        - kat1 - float - количество расхода катализатора 1
        - kat2 - float - количество расхода катализатора 2
        - kat3 - float - количество расхода катализатора 3
        - date - Date - дата

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
        Сущность для определения сумарного расхода энергоресурсов

          Attributes
        ===========
        - input1 - float - расход эл.энергии ввода 1
        - input2 - float - расход эл.энергии ввода 2
        - gas - float - расход газа
        - date - Date - дата

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
        - iso - float - количество удельного расхода изоцианата
        - pol - float - количество удельного расхода полиола
        - pen - float - количество удельного расхода пентана
        - kat1 - float - количество удельного расхода катализатора 1
        - kat2 - float - количество удельного расхода катализатора 2
        - kat3 - float - количество удельного расхода катализатора 3
        - date - Date - дата

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