from django.core.exceptions import ValidationError
from django.db import models, connection
from structure.models import Sensors
import datetime
from django.utils.translation import ugettext_lazy as _

from users.models import UserP


class Workspace(models.Model):
    """
    Сущность для сохранения рабочих пространств для пользователя в рекордере
    """
    name = models.CharField(max_length=255, default='workspace')
    parent = models.ForeignKey(UserP, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    unit = models.CharField(max_length=255, default='')
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

        now = datetime.datetime.now().time().strftime('%H:%M:%S')
        now_t = datetime.datetime.now()
        shifts = self.sensor.parent.parent.shift_set.filter(start__lte=now, end__gt=now)
        if not shifts:
            return self.get_last_day()
        start = datetime.datetime(now_t.year, now_t.month, now_t.day, shifts[0].start.hour, shifts[0].start.minute, 0)
        end = datetime.datetime(now_t.year, now_t.month, now_t.day, shifts[0].end.hour, shifts[0].end.minute, 0)
        return self._time_conversion(start=start, end=end)

    def get_last_day(self) -> object:
        """метод возвращает данные за последний день"""
        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        start = now - datetime.timedelta(days=1)
        return self._time_conversion(start=start, end=now)

    def get_last_week(self) -> object:
        """метод возвращает данные за последнию неделю"""
        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        start = now - datetime.timedelta(days=7)
        return self._time_conversion(start=start, end=now)

    def get_last_month(self) -> object:
        """метод возвращает данные за последний месяц"""
        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        start = now - datetime.timedelta(days=30)
        return self._time_conversion(start=start, end=now)

    def get_last_hour(self) -> object:
        """возвращает значения за последний час"""
        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        start = end - datetime.timedelta(hours=4)

        return self._time_conversion(start=start, end=end)

    def _time_conversion(self, start, end) -> object:
        """
        преобразование времени к формату
        :param datetime start: начало периода
        :param datetime end: конец периода

        """
        f = '%Y-%m-%d %H:%M:%S'
        start = start.strftime(f)
        end = end.strftime(f)
        return self.get_period(start=start, end=end)

    def get_period(self, start, end) -> list:
        """метод возвращает данные за период start - end

        :param datetime start: начало периода
        :param datetime end: конец периода
        :return: list
        """
        f = '%Y-%m-%d %H:%M:%S'
        if (((datetime.datetime.strptime(end,f) - datetime.datetime.strptime(start,f))) < datetime.timedelta(hours=6)):
            curs = connection.cursor()
            curs.execute(
                f"""SELECT (now_time +('180 minute'::interval))::timestamp, key, value FROM {str(self.table_name)} WHERE now_time >= '{
                str(start)}' AND now_time<'{str(end,)}';""")
            query = curs.fetchall()
            fieldnames = [name[0] for name in curs.description]
            result = []
            for row in query:
                rowset = []
                for field in zip(fieldnames, row):
                    rowset.append(field)
                result.append(dict(rowset))
            return result
        else:
            a = self._generate_period_min(start, end)
            # return self._get_mode_by_periods(var=a['var'], periods=a['periods'])
            return self.get_mode_by_periods_interval(start=start, end=end, interval=a['var'])

    def _generate_period_min(self, start, end) -> dict:
        """
        пересчитывает время в интервалы для метода моды и среднего исходя из заданного количество точек points

        :param real start: начало периода
        :param real end: конец периода
        :return: dict {'var':real,'periods':real}
        """
        f = '%Y-%m-%d %H:%M:%S'
        points = 200  # количество точек
        minutes = (datetime.datetime.strptime(end,f)- datetime.datetime.strptime(start,f)).total_seconds() / 60
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
        query = curs.fetchall()
        fieldnames = [name[0] for name in curs.description]
        result = []
        for row in query:
            rowset = []
            for field in zip(fieldnames, row):
                rowset.append(field)
            result.append(dict(rowset))
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
            "SELECT a.start_time, a.end_time, (SELECT mode() WITHIN GROUP (ORDER BY value) as modevar" \
            " FROM " + str(self.table_name) + \
            " r WHERE  r.now_time>=a.start_time and r.now_time<a.end_time) as value from " + str(
            self.table_name) + " b right join " \
                               "period_t a ON b.now_time>=a.start_time AND b.now_time<a.end_time GROUP BY a.start_time, a.end_time" \
                               " ORDER BY a.start_time desc"
        try:
            curs.execute(sql)
        except Exception as a:
            return False
        query = curs.fetchall()
        fieldnames = [name[0] for name in curs.description]
        result = []
        for row in query:
            rowset = []
            for field in zip(fieldnames, row):
                rowset.append(field)
            result.append(dict(rowset))
        return result


    def get_mode_by_periods_interval(self, start, end, interval=20) -> list or bool:

        curs = connection.cursor()
        sql = "with period_t as (SELECT n as ti from generate_series('" + str(start) + "'::timestamp,'" + str(
                end) + "'::timestamp,'" + str(interval) + " minute'::interval) n)" \
            "SELECT ti as now_time, COALESCE((SELECT mode() WITHIN GROUP (ORDER BY value) as modevar" \
            " FROM " + str(self.table_name) + \
            " r WHERE  r.now_time>=ti and r.now_time<(ti+('"+str(interval)+ \
            " minutes'::interval))),NULL) as value from " \
              + str(self.table_name) + " b right join " \
            "period_t a ON b.now_time>=ti AND b.now_time<(ti+('"+str(interval)+" minutes'::interval)) GROUP BY ti" \
            " ORDER BY ti desc"
        try:
            curs.execute(sql)
        except Exception as a:
            return a.__str__()
        query = curs.fetchall()
        fieldnames = [name[0] for name in curs.description]
        result = []
        for row in query:
            rowset = []
            for field in zip(fieldnames, row):
                rowset.append(field)
            result.append(dict(rowset))
        if(result[0]['value']==None):
            result[0]['value'] = 0
        return result


class Workarea(models.Model):
    """
    Сущность для определения рабочего пространства

     Attributes
    ============

    - name - название рабочего пространнства
    - parent - FK для рабочей области
    - data - FK для связи точки с данными

     Methods
    ========

    none

    """
    name = models.CharField(max_length=255, default='workarea')
    parent = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    data = models.ManyToManyField(ValueSensor, through='WorkareaData',through_fields=('workarea', 'value'),)

    def __str__(self):
        return self.name

class WorkareaData(models.Model):
    """
    сущнсть для связи многие ко многим сущности рабочего пространнства и сущнсть данных сенсора
    """
    workarea = models.ForeignKey(Workarea, on_delete=models.CASCADE)
    value = models.ForeignKey(ValueSensor, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, default='#000000')

    def __str__(self):
        return self.workarea.name +"-" +self.value.name