import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from datetime import datetime

from django.db.models import CharField
from rest_framework.exceptions import ValidationError


class JSONField(models.TextField):
    """
    JSONField es un campo TextField que serializa/deserializa objetos JSON.
    Django snippet #1478

    Ejemplo:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)

        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """
    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value


class FirstObject(models.Model):
    """
    Предназначена для создания структуры предприятя исходя из полей заполненых пользователем

     Attributes
    ===========

    - name -  поле для строкового обозначения структуры
    - customer - название заказчика
    - contract - название контракта
    - date_add - дата создания
    - date_update - дата обновления
    - structure - сформированная структура в формате JSON

     Methods
    =========

    - none

    """
    name = models.CharField(max_length=255, default='no name')
    customer = models.CharField(max_length=255, default='no customer')
    contract = models.CharField(max_length=255, default='no contract')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    structure = JSONField(null=True, blank=True)
    start_object = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Reserv_1(models.Model):
    """
    Резервный класс для структуры предприятия

     Attributes
    ===========

    - name - str - название для резевной структуры

     Methods
    =============

    - none

    """
    name = models.CharField(max_length=255, default='Базавая структуру')
    def __str__(self):
        return self.name

    def save(self):
        ob = FirstObject.objects.all().first()

        if (ob):
            ob.start_object = self.pk
            ob.save()
            super(Reserv_1, self).save()
        else:
            raise ValidationError('No structure in ferststructure',
                                  code='invalid'
                                  )



class Reserv_2(models.Model):
    """
    Резервный класс для структуры предприятия

     Attributes
    ===========

    - name - str - название для резевной структуры
    - res1 - FK - внешний ключ для связи с резервной таблицой Reserv_1

     Methods
    =============

    - none

    """
    name = models.CharField(max_length=255, default='no name')
    parent = models.ForeignKey(Reserv_1, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Corparation(models.Model):
    """
    Сущность для определения объединения в структуре предпрития (если выбрано в FirstObject)

     Attributes
    ===========

    - name - str - название записи
    - res2 - FK - внешний ключ для связи с резервной таблицой Reserv_2

     Methods
    =============

    - none

    """
    name = models.CharField(max_length=255, default='Базавая структуру')
    parent = models.ForeignKey(Reserv_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Company(models.Model):
    """
    Сущность для определения огранизации в структуре предпрития (если выбрано в FirstObject)

     Attributes
    ===========

    - name - str - название записи
    - corp - FK - внешний ключ для связи с сущностью  Corparation


     Methods
    =============

    - none

    """
    name = models.CharField(max_length=255, default='Базавая структуру')
    parent = models.ForeignKey(Corparation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Factory(models.Model):
    """
    Сущность для определения завода в структуре предпрития (если выбрано в FirstObject)


     Attributes
    ===========

    - name - str - название записи
    - comp - FK - внешний ключ для связи с сущностью  Company
    - address - str - поля для адреса завода


     Methods
    =============

    - none

    """
    parent = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')
    address = models.CharField(max_length=255, default='no address')

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Сущность для определения цеха на заводе в структуре предпрития (если выбрано в FirstObject)


     Attributes
    ===========

    - name - str - название записи
    - factory - FK - внешний ключ для связи с сущностью  Factory

     Methods
    =============

    - now_shift - возвращает текущую смену департамента

    """
    parent = models.ForeignKey(Factory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')

    def __str__(self):
        return self.name

    def now_shift(self) -> list:
        """возвращает текущую смену департамента как list с вложенным словарем"""
        now = datetime.now().time().strftime('%H:%M:%S')
        shift = self.shift_set.filter(start__lt=now, end__gte=now)
        return shift


class Shift(models.Model):
    """
    Сущность для определения смен в цеху в структуре предпрития (если выбрано в FirstObject)

     Attributes
    ===========

    - name - str - название записи
    - dep - FK - внешний ключ для связи с сущностью  Department
    - start - time - начало смены
    - end - time -  конец смены

     Methods
    =============

    - all_shift_now - возвращает текущие смены всех департаментов

    """
    parent = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')
    start = models.TimeField('start shift')
    end = models.TimeField('end shift')

    def __str__(self):
        return self.name

    def all_shift_now(self) -> list:
        """возвращает текущие смены всех департаментов"""
        now = datetime.time(datetime.now())
        shift = Shift.objects.filter(start__lt=now, end__gte=now)
        return shift




class Lunch(models.Model):
    """
    Сущность для определения смен в цеху в структуре предпрития (если выбрано в FirstObject)

     Attributes
    ===========

    - name - str - название для записи
    - shift - FK - внешний ключ для связи с сущностью  Shift
    - start - time - начало обеда
    - end - time -  конец конец обеда

     Methods
    =============

    - None

    """
    parent = models.ForeignKey(Shift, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')
    start = models.TimeField('start shift')
    end = models.TimeField('end shift')

    def __str__(self):
        return self.name


class Agreagat(models.Model):
    """
    Сущность для определения оборудования в цеху

     Attributes
    ===========

    - name - str - название для записи
    - dep - FK - внешний ключ для связи с сущностью  Department

     Methods
    =============

    - None

    """
    parent = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')

    def __str__(self):
        return self.name


class Sensors(models.Model):
    """
    Сущность для определения датчика на оборудовании

     Attributes
    ===========

    - name - str - название для записи
    - agregat - FK - внешний ключ для связи с сущностью  Agreagat
    - designation - str - обозначение на схеме

     Methods
    =============

    - get_parent - возвращает объект Agregat родителя датчика

    """
    parent = models.ForeignKey(Agreagat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Базавая структуру')
    designation = models.CharField(max_length=255, default='no designation')

    def __str__(self):
        return self.name

    def get_parent(self) -> object:
        """возвращает родителя для данного датчика"""
        return self.parent
