from project_v_0_0_1.settings import dist_table
from django.db import connection
from django.db import utils


def decorator_exists(func):
    '''
    Декоратор для ошибки на отсутстви таблицы
    '''
    def wrapper(*args, **kwargs):
        try:
            a = func(*args, **kwargs)
        except utils.OperationalError:
            a = 'Таблица не найдена'
            print(a)
        return a
    return wrapper




class TransitionReadings(object):
    '''
    Класс для виджета Показания перехода

    Methods
       =============
       - __selectfrom - вывод велечины value последней записи таблицы
       - methane - возвращает последнее количество метана
       - carbondioxide - возвращает последнее количество углекислого газа
       - oxygen - возвращает последнее количество кислорода
       - pressure_in - возвращает последнее значение давления Pвых компр
       - pressure_out - возвращает последнее значение давления Pвх генер
       - consumption - возвращает последнее значение расхода
       - temperature - возвращает последнее значение температуры
    '''

    @decorator_exists
    def __selectfrom(self, st):
        '''
        Возвращает велечины value последней записи таблицы

        :param str st: имя таблицы
        '''
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + st + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a



    def methane(self):
        '''
        Возвращает последнее количество метана
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['methane'])
        if a is None:
            a = [0]
        return a[0]

    def carbondioxide(self):
        '''
        Возвращает последнее количество углекислого газа
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['сarbon dioxide'])
        if a is None:
            a = [0]
        return a[0]

    def oxygen(self):
        '''
        Возвращает последнее количество кислорода
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['oxygen'])
        if a is None:
            a = [0]
        return a[0]

    def pressure_in(self):
        '''
        Возвращает последнее значение давления Pвых компр
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure in'])
        if a is None:
            a = [0]
        return a[0]

    def pressure_out(self):
        '''
        Возвращает последнее значение давления Pвх генер
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure out'])
        if a is None:
            a = [0]
        return a[0]

    def consumption(self):
        '''
        Возвращает последнее значение расхода
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['consumption'])
        if a is None:
            a = [0]
        return a[0]

    def temperature(self):
        '''
        Возвращает последнее значение температуры
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['temperature'])
        if a is None:
            a = [0]
        return a[0]



class GenerationOfElectricity(object):
    '''
    Класс для виджета Выработка электроэнергии

    Methods
       =============
       - __selectfrom - вывод велечины value последней записи таблицы
       - machine1 - возвращает последнее значение мощности машины 1
       - machine2 - возвращает последнее значение мощности машины 2
       - machine3 - возвращает последнее значение мощности машины 3
       - machine4 - возвращает последнее значение мощности машины 4
       - sum - возвращает сумму мощностей 4-х машин

    '''

    @decorator_exists
    def __selectfrom(self, text):
        '''
        Возвращает велечины value последней записи таблицы

        :param str st: имя таблицы
        '''
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + text + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a

    def machine1(self):
        '''
        Возвращает последнее значение мощности машины 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 1'])
        if a is None:
            a = [0]
        return a[0]

    def machine2(self):
        '''
        Возвращает последнее значение мощности машины 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 2'])
        if a is None:
            a = [0]
        return a[0]

    def machine3(self):
        '''
        Возвращает последнее значение мощности машины 3
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 3'])
        if a is None:
            a = [0]
        return a[0]

    def machine4(self):
        '''
        Возвращает последнее значение мощности машины 4
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 4'])
        if a is None:
            a = [0]
        return a[0]

    def sum(self):
        '''
        Возвращает сумму мощностей 4-х машин
        '''
        a = self.machine1() + self.machine2() + self.machine3() + self.machine4()
        return a

class Status(object):
    '''
    Класс для виджетов Режим работы, Насосы, Задвижки, Компрессоры, Машины

    Methods
       =============
       - __selectfrom - вывод велечины value последней записи таблицы
       - mode - возвращает информацию о режиме работы
       - damper1 - возвращает информацию о состаянии задвижки 1
       - damper2 - возвращает информацию о состаянии задвижки 2
       - pump - возвращает информацию о состаянии насоса
       - compress1 - возвращает информацию о состаянии компрессора 1
       - compress2 - возвращает информацию о состаянии компрессора 2
       - compress3 - возвращает информацию о состаянии компрессора 3
       - generator1 - возвращает информацию о состаянии генератора 1
       - generator2 - возвращает информацию о состаянии генератора 2
       - generator3 - возвращает информацию о состаянии генератора 3
       - generator4 - возвращает информацию о состаянии генератора 4
       - torch - возвращает информацию о состаянии факела

    '''

    @decorator_exists
    def __selectfrom(self, text):
        '''
        Возвращает велечины value последней записи таблицы

        :param str st: имя таблицы
        '''
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + text + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a

    def mode(self):
        '''
        Возвращает информацию о режиме работы
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Mode'])
        if a[0] == 1:
            k = "Автоматический режим"
        else:
            k = "Ручной режим"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def damper1(self):
        '''
        Возвращает информацию о состаянии задвижки 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam1'])
        if a[0] == 1:
            k = "Открыта"
        else:
            k = "Закрыта"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def damper2(self):
        '''
        Возвращает информацию о состаянии задвижки 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam2'])
        if a[0] == 1:
            k = "Открыта"
        else:
            k = "Закрыта"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def pump(self):
        '''
        Возвращает информацию о состаянии насоса
        '''
        b = self.__selectfrom(dist_table['Taldefax']['Pump']['Status'])
        if b[0] == 1:
            k = "Работа"
        else:
            k = "Остановлен"
        a = self.__selectfrom(dist_table['Taldefax']['Pump']['Alarm'])
        if a[0] == 1:
            k = "Авария"
        a = {
            "alarm": a[0],
            "work": b[0],
            "text": k
        }
        return a

    def compress1(self):
        '''
        Возвращает информацию о состаянии компрессора 1
        '''
        b = self.__selectfrom(dist_table['Taldefax']['Compress']['compress1']['Status'])
        if b[0] == 1:
            k = "Работа"
        else:
            k = "Остановлен"
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress1']['Alarm'])
        if a[0] == 1:
            k = "Авария"
        a = {
            "alarm": a[0],
            "work": b[0],
            "text": k
        }
        return a

    def compress2(self):
        '''
        Возвращает информацию о состаянии компрессора 2
        '''
        b = self.__selectfrom(dist_table['Taldefax']['Compress']['compress2']['Status'])
        if b[0] == 1:
            k = "Работа"
        else:
            k = "Остановлен"
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress2']['Alarm'])
        if a[0] == 1:
            k = "Авария"
        a = {
            "alarm": a[0],
            "work": b[0],
            "text": k
        }
        return a

    def compress3(self):
        '''
        Возвращает информацию о состаянии компрессора 3
        '''
        b = self.__selectfrom(dist_table['Taldefax']['Compress']['compress3']['Status'])
        if b[0] == 1:
            k = "Работа"
        else:
            k = "Остановлен"
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress3']['Alarm'])
        if a[0] == 1:
            k = "Авария"
        a = {
            "alarm": a[0],
            "work": b[0],
            "text": k
        }
        return a

    def generator1(self):
        '''
        Возвращает информацию о состаянии генератора 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator1'])
        if a[0] == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def generator2(self):
        '''
        Возвращает информацию о состаянии генератора 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator2'])
        if a[0] == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def generator3(self):
        '''
        Возвращает информацию о состаянии генератора 3
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator3'])
        if a[0] == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def generator4(self):
        '''
        Возвращает информацию о состаянии генератора 4
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator4'])
        if a[0] == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        a = {
            "status": a[0],
            "text": k
        }
        return a

    def torch(self):
        '''
        Возвращает информацию о состаянии факела
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['torch'])
        if a[0] == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        a = {
            "status": a[0],
            "text": k
        }
        return a