from django.db import models
from datetime import datetime


class Reserv_1(models.Model):
    name = models.CharField(max_length=255, default='no name')


class Reserv_2(models.Model):
    name = models.CharField(max_length=255, default='no name')
    res1 = models.ForeignKey(Reserv_1, on_delete=models.CASCADE)


class Corparation(models.Model):
    name = models.CharField(max_length=255, default='no name')
    res2 = models.ForeignKey(Reserv_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Factory(models.Model):
    corp = models.ForeignKey(Corparation, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')

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
