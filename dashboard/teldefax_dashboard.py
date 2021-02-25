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
        except utils.ProgrammingError:
            a = 'Таблица не найдена'
        return a
    return wrapper



def _check_the_data_single(a):
    if a is None:
        a = [0]
    if type(a[0]) == str:
        return a
    else:
        return a[0]

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

    def get_frequece_compressors(self, name):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['methane'])
        return _check_the_data_single(a)

    def methane(self):
        '''
        Возвращает последнее количество метана
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['methane'])
        return _check_the_data_single(a)

    def carbondioxide(self):
        '''
        Возвращает последнее количество углекислого газа
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['сarbon dioxide'])
        return _check_the_data_single(a)

    def oxygen(self):
        '''
        Возвращает последнее количество кислорода
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['oxygen'])
        return _check_the_data_single(a)

    def pressure_in(self):
        '''
        Возвращает последнее значение давления Pвых компр
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure in'])
        return _check_the_data_single(a)

    def pressure_out(self):
        '''
        Возвращает последнее значение давления Pвх генер
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure out'])
        return _check_the_data_single(a)

    def consumption(self):
        '''
        Возвращает последнее значение расхода
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['consumption'])
        return _check_the_data_single(a)

    def temperature(self):
        '''
        Возвращает последнее значение температуры
        '''
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['temperature'])
        return _check_the_data_single(a)



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

    def machine1(self) -> str or float or int:
        '''
        Возвращает последнее значение мощности машины 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 1'])
        return _check_the_data_single(a)

    def machine2(self) -> str or float or int:
        '''
        Возвращает последнее значение мощности машины 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 2'])
        return _check_the_data_single(a)

    def machine3(self) -> str or float or int:
        '''
        Возвращает последнее значение мощности машины 3
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 3'])
        return _check_the_data_single(a)

    def machine4(self) -> str or float or int:
        '''
        Возвращает последнее значение мощности машины 4
        '''
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 4'])
        return _check_the_data_single(a)

    def sum(self) -> int or float:
        '''
        Возвращает сумму мощностей 4-х машин
        '''
        list_ = [self.machine1(), self.machine2(), self.machine3(), self.machine4()]
        list_ = list(map(lambda x: 0 if type(x)==str else x, list_))
        return sum(list_)

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

    def __check_result_single(self, a, text1: str = 'состояние True', text2: str = "состояние False") -> str or dict:
        """проверка условия наличия таблицы и режима работы

        :param str text1: текста для состояния 1
        :param str text2:  текст для состояние 0

        """
        if a == "Таблица не найдена":
            return a
        else:
            if a[0] == 1:
                k = text1
            else:
                k = text2
            a = {
                "status": a[0],
                "text": k
            }
            return a

    def mode(self):
        '''
        Возвращает информацию о режиме работы
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Mode'])
        text1 = "Автоматический режим"
        text2 = "Ручной режим"
        return self.__check_result_single(a, text1, text2)

    def damper1(self):
        '''
        Возвращает информацию о состаянии задвижки 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam1'])
        text1 = "Открыта"
        text2 = "Закрыта"
        return self.__check_result_single(a, text1, text2)

    def damper2(self):
        '''
        Возвращает информацию о состаянии задвижки 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam2'])
        text1 = "Открыта"
        text2 = "Закрыта"
        return self.__check_result_single(a, text1, text2)

    def __check_result_many(self, t_status, t_alarm) -> dict:
        """проверка статусов работы компрессоров и насоса

        :param str t_status: таблица с сотоянием статуса
        :param str t_alarm: таблица с сотоянием аварии

        """
        b = self.__selectfrom(t_status)
        k = "Таблица не найдена"
        if b != "Таблица не найдена":
            if b[0] == 1:
                k = "Работа"
                work = b[0]
            else:
                k = "Остановлен"
                work = b[0]
        else:
            work = "Таблица не найдена"
        a = self.__selectfrom(t_alarm)
        if a != "Таблица не найдена":
            if a[0] == 1:
                k = "Авария"
                alarm = a[0]
            else:
                alarm = a[0]
        else:
            alarm = "Таблица не найдена"
        a = {
            "alarm": alarm,
            "work": work,
            "text": k
        }
        return a

    def pump(self):
        '''
        Возвращает информацию о состаянии насоса
        '''
        return self.__check_result_many(dist_table['Taldefax']['Pump']['Status'],dist_table['Taldefax']['Pump']['Alarm'])


    def compress1(self):
        '''
        Возвращает информацию о состаянии компрессора 1
        '''
        return self.__check_result_many(dist_table['Taldefax']['Compress']['compress1']['Status'],
                                        dist_table['Taldefax']['Compress']['compress1']['Alarm'])


    def compress2(self):
        '''
        Возвращает информацию о состаянии компрессора 2
        '''
        return self.__check_result_many(dist_table['Taldefax']['Compress']['compress2']['Status'],
                                        dist_table['Taldefax']['Compress']['compress2']['Alarm'])


    def compress3(self):
        '''
        Возвращает информацию о состаянии компрессора 3
        '''
        return self.__check_result_many(dist_table['Taldefax']['Compress']['compress3']['Status'],
                                        dist_table['Taldefax']['Compress']['compress3']['Alarm'])


    def generator1(self):
        '''
        Возвращает информацию о состаянии генератора 1
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator1'])
        text1 = "Авария Остановлен"
        text2 = "Работа Генерация"
        return self.__check_result_single(a, text1, text2)

    def generator2(self):
        '''
        Возвращает информацию о состаянии генератора 2
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator2'])
        text1 = "Авария Остановлен"
        text2 = "Работа Генерация"
        return self.__check_result_single(a, text1, text2)

    def generator3(self):
        '''
        Возвращает информацию о состаянии генератора 3
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator3'])
        text1 = "Авария Остановлен"
        text2 = "Работа Генерация"
        return self.__check_result_single(a, text1, text2)

    def generator4(self):
        '''
        Возвращает информацию о состаянии генератора 4
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator4'])
        text1 = "Авария Остановлен"
        text2 = "Работа Генерация"
        return self.__check_result_single(a, text1, text2)

    def torch(self):
        '''
        Возвращает информацию о состаянии факела
        '''
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['torch'])
        text1 = "Авария Остановлен"
        text2 = "Работа Генерация"
        return self.__check_result_single(a, text1, text2)