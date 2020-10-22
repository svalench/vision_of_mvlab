from django.db import models, connection
from structure.models import Sensors
from datetime import datetime


class ValueSensor(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='no name')
    name_connection = models.CharField(max_length=255, default='no name connection')
    table_name = models.CharField(max_length=255, default='no table name')
    up_level_alarm = models.FloatField(default=0.00)
    down_level_alarm = models.FloatField(default=0.00)
    up_level = models.FloatField(default=0.00)
    down_level = models.FloatField(default=0.00)
    rate_change = models.FloatField(default=0.00)

    def __str__(self):
        return self.name

    def get_period(self, start, end):
        curs = connection.cursor()
        curs.execute(
            "SELECT * FROM `" + str(self.table_name) + "` WHERE now_time >= " +
            str(start) + " AND now_time<" + str(end) + ";")
        result = curs.fetchall()
        return result

    def get_last_shift(self):
        now = datetime.now().time().strftime('%H:%M:%S')
        shifts = self.sensor.agregat.dep.shift_set.filter(start__lte=now, end__gt = now)
        dn = datetime(now.year, now.month, now.day, shifts[0].start.hour, shifts[0].start.minute, 0)
        de = datetime(now.year, now.month, now.day, shifts[0].end.hour, shifts[0].end.minute, 0)
        start = (dn - datetime(1970, 1, 1)).total_seconds()
        end = (de - datetime(1970, 1, 1)).total_seconds()
        return self.get_period(start=start, end=end)
