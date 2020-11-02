import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from datetime import datetime


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
    name = models.CharField(max_length=255, default='no name')
    customer = models.CharField(max_length=255, default='no customer')
    contract = models.CharField(max_length=255, default='no contract')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    structure = JSONField(null=True, blank=True)
    def __str__(self):
        return self.name

class Reserv_1(models.Model):
    name = models.CharField(max_length=255, default='no name')
    def __str__(self):
        return self.name


class Reserv_2(models.Model):
    name = models.CharField(max_length=255, default='no name')
    res1 = models.ForeignKey(Reserv_1, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Corparation(models.Model):
    name = models.CharField(max_length=255, default='no name')

    res2 = models.ForeignKey(Reserv_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Factory(models.Model):
    corp = models.ForeignKey(Corparation, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')
    address = models.CharField(max_length=255, default='no address')

    def __str__(self):
        return self.name


class Department(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')

    def __str__(self):
        return self.name

    def now_shift(self) -> object:
        """возвращает текущую смену департамента"""
        now = datetime.now().time().strftime('%H:%M:%S')
        shift = self.shift_set.filter(start__lt=now, end__gte=now)
        return shift


class Shift(models.Model):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')
    start = models.TimeField('start shift')
    end = models.TimeField('end shift')

    def __str__(self):
        return self.name

    def all_shift_now(self) -> object:
        """возвращает текущие смены всех департаментов"""
        now = datetime.time(datetime.now())
        shift = Shift.objects.filter(start__lt=now, end__gte=now)
        return shift




class Lunch(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')
    start = models.TimeField('start shift')
    end = models.TimeField('end shift')

    def __str__(self):
        return self.name


class Agreagat(models.Model):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')

    def __str__(self):
        return self.name


class Sensors(models.Model):
    agregat = models.ForeignKey(Agreagat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')
    designation = models.CharField(max_length=255, default='no designation')

    def __str__(self):
        return self.name

    def get_parent(self):
        return self.agregat
