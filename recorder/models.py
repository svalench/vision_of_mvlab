from django.core.exceptions import ValidationError
from django.db import models, connection
from structure.models import Sensors
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class ValueSensor(models.Model):
    """класс предназначен для связи модели структуры Джанго и модуля сбора данных

     Attributes
    ============

    - sensor - FK - внешний ключ к сущности Sensors
    - name - str - название переменной
    - name_connection - str - название соединения
    - table_name - str - название иаблицы с данными
    - up_level_alarm - float - верхний уроыень аварии
    - down_level_alarm - float - нижний уровень аварии
    - up_level - float - верхний придел
    - down_level - float - нижниц придел
    ===================

      Methods
    ============

    - get_last_shift - возвращает list  с данными за текущую смену (без усреднения)
    - get_last_day - возвращает list  с данными за текущий день (без усреднения)
    - get_last_hour - возвращает list  с данными за текущий час (без усреднения)
    - _time_conversion - метод преобразования формата времени (protected)
    - get_period - метод получения данных в промежутке start=<start_time> до end=<end_period>
    ===============

    """
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

    def save(self, *args, **kwargs):
        if self._check_table_name(str(self.table_name)):
            super(ValueSensor, self).save(*args, **kwargs)
        else:
            raise ValidationError(_('Table with this name = "%s" does not exist'),
                                  params=(self.table_name,),
                                  code='invalid'
                                  )

    def get_last_shift(self) -> object:
        """метод возвращает данные за текущую смену"""
        now = datetime.now().time().strftime('%H:%M:%S')
        now_t = datetime.now().time()
        shifts = self.sensor.agregat.parent.shift_set.filter(start__lte=now, end__gt=now)
        start = datetime(now_t.year, now_t.month, now_t.day, shifts[0].start.hour, shifts[0].start.minute, 0)
        end = datetime(now_t.year, now_t.month, now_t.day, shifts[0].end.hour, shifts[0].end.minute, 0)
        return self._time_conversion(start=start, end=end)

    def get_last_day(self) -> object:
        """метод возвращает данные за последний день"""
        now = datetime.now().time()
        start = datetime(now.year, now.month, now.day, now.hour - 24, now.minute, 0)
        end = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        return self._time_conversion(start=start, end=end)

    def get_last_hour(self) -> object:
        """возвращает значения за последний час"""
        now = datetime.now().time()
        start = datetime(now.year, now.month, now.day, now.hour, now.minute - 60, 0)
        end = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        return self._time_conversion(start=start, end=end)

    def _time_conversion(self, start, end) -> object:
        """
        преобразование времени к формату
        :param datetime start: начало периода
        :param datetime end: конец периода

        """
        start = (start - datetime(1970, 1, 1)).total_seconds()
        end = (end - datetime(1970, 1, 1)).total_seconds()
        return self.get_period(start=start, end=end)

    def get_period(self, start, end) -> list:
        """метод возвращает данные за период start - end

        :param float start: начало периода
        :param float end: конец периода
        :return: list
        """
        if (((end - start) / 60) < 100):
            curs = connection.cursor()
            curs.execute(
                "SELECT * FROM `" + str(self.table_name) + "` WHERE now_time >= " +
                str(start) + " AND now_time<" + str(end) + ";")
            result = curs.fetchall()
            return result
        else:
            a = self._generate_period_min(start, end)
            return self._get_mode_by_periods(var=a['var'], periods=a['period'])

    def _generate_period_min(self, start, end) -> dict:
        """
        пересчитывает время в интервалы для метода моды и среднего исходя из заданного количество точек points

        :param real start: начало периода
        :param real end: конец периода
        :return: dict {'var':real,'periods':real}
        """
        points = 100  # количество точек
        minutes = (end - start) / 60
        interval = minutes / points
        return {'var': interval, 'periods': minutes}

    def _check_table_name(self, name):
        """проверка на наличие таблицы с  именем <name>
        :param str name: название таблицы

        """
        engine = connection.vendor
        curs = connection.cursor()
        if (engine == 'sqlite'):
            curs.execute("SELECT name FROM  'sqlite_master' WHERE type ='table' AND name=%s;", [str(name)])
        elif (engine == 'postgresql'):
            try:
                curs.execute("SELECT table_name FROM "
                             " information_schema.tables WHERE table_schema = 'public' "
                             " AND table_name =%s;", [str(name)])
            except:
                return False
        else:
            return False
        result = curs.fetchall()
        if len(result) == 0:
            return False
        else:
            return True

    def _get_average_by_periods(self, var=5, periods=100) -> list or bool:
        """
        Возвращет объект с усреднеными значениями из периода periods (в минутах) разбитый по частям на интервалы var минут

        :param int var: шаг в минутах
        :param int periods: интервал в минутах
        :return: list [{'start_time':datetime,'end_time':datetime,'value':real}]
        :raises ValueError: Вернет False
        """
        curs = connection.cursor()
        sql = "with period_t as (" \
              "SELECT" \
              "(SELECT max(now_time)::timestamp from " + str(self.table_name) + ")+((n-" + str(
            var) + ") || 'minutes')::interval start_time," \
                   "(SELECT max(now_time)::timestamp from " + str(
            self.table_name) + ")+(n || 'minutes')::interval end_time " \
                               "from generate_series(0,-" + str(periods) + ",-" + str(var) + ") n" \
                                                                                             ")" \
                                                                                             "SELECT a.start_time, a.end_time, AVG(b.value) as value from " + str(
            self.table_name) + " b right join" \
                               "period_t a ON b.now_time>=a.start_time AND b.now_time<a.end_time GROUP BY a.start_time, a.end_time" \
                               "ORDER BY a.start_time desc"
        try:
            curs.execute(sql)
        except:
            return False
        result = curs.fetchall()
        return result

    def _get_mode_by_periods(self, var=5, periods=100) -> list or bool:
        """
        Возвращет объект со значениями по МОДЫ из периода periods (в минутах) разбитый по частям на интервалы var минут

        :param int var: шаг в минутах
        :param int periods: интервал в минутах
        :return: list [{'start_time':datetime,'end_time':datetime,'modevar':real}]
        :raises ValueError: Вернет False
        """
        curs = connection.cursor()
        sql = "with period_t as (" \
              "SELECT" \
              "(SELECT max(now_time)::timestamp from " + str(self.table_name) + ")+((n-" + str(
            var) + ") || 'minutes')::interval start_time," \
                   "(SELECT max(now_time)::timestamp from " + str(
            self.table_name) + ")+(n || 'minutes')::interval end_time " \
                               "from generate_series(0,-" + str(periods) + ",-" + str(var) + ") n" \
                                                                                             ")" \
                                                                                             "SELECT a.start_time, a.end_time, (SELECT mode() WITH GROUP (ORDER BY value) as modevar" \
                                                                                             " FROM " + str(
            self.table_name) + " r WHERE  r.now_time>=f.start_time and r.now_time<f.end_time) as value from " + str(
            self.table_name) + " b right join" \
                               "period_t a ON b.now_time>=a.start_time AND b.now_time<a.end_time GROUP BY a.start_time, a.end_time" \
                               "ORDER BY a.start_time desc"
        try:
            curs.execute(sql)
        except:
            return False
        result = curs.fetchall()
        return result
