from project_v_0_0_1.settings import dist_table
from django.db import connection
from django.db import utils


def decorator_exists(func):
    def wrapper(*args, **kwargs):
        try:
            a = func(*args, **kwargs)
        except utils.OperationalError:
            a = 'Таблица не найдена'
            print(a)
        return a
    return wrapper




class TransitionReadings(object):

    @decorator_exists
    def __selectfrom(self, st):
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + st + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a



    def methane(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['methane'])
        if a is None:
            a = 0
        return a

    def carbondioxide(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['сarbon dioxide'])
        if a is None:
            a = 0
        return a

    def oxygen(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['oxygen'])
        if a is None:
            a = 0
        return a

    def pressure_in(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure in'])
        if a is None:
            a = 0
        return a

    def pressure_out(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['pressure out'])
        if a is None:
            a = 0
        return a

    def consumption(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['consumption'])
        if a is None:
            a = 0
        return a

    def temperature(self):
        a = self.__selectfrom(dist_table['Taldefax']['TransitionReadings']['temperature'])
        if a is None:
            a = 0
        return a



class GenerationOfElectricity(object):
    sql1 = '''SELECT value FROM '''
    sql2 = ''' ORDER BY now_time DESC LIMIT 1'''

    @decorator_exists
    def __selectfrom(self, text):
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + text + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a

    def machine1(self):
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 1'])
        if a is None:
            a = 0
        return a

    def machine2(self):
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 2'])
        if a is None:
            a = 0
        return a

    def machine3(self):
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 3'])
        if a is None:
            a = 0
        return a

    def machine4(self):
        a = self.__selectfrom(dist_table['Taldefax']['GenerationOfElectricity']['machine 4'])
        if a is None:
            a = 0
        return a

class Status(object):

    @decorator_exists
    def __selectfrom(self, text):
        with connection.cursor() as cursor:
            sql1 = '''SELECT value FROM '''
            sql2 = ''' ORDER BY now_time DESC LIMIT 1'''
            sql = sql1 + text + sql2
            cursor.execute(sql)
            a = cursor.fetchone()
        return a

    def mode(self):
        a = self.__selectfrom(dist_table['Taldefax']['Mode'])
        if a == 1:
            k = "Автоматический режим"
        else:
            k = "Ручной режим"
        return k

    def damper1(self):
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam1'])
        if a == 1:
            k = "Открыта"
        else:
            k = "Закрыта"
        return k

    def damper2(self):
        a = self.__selectfrom(dist_table['Taldefax']['Damper']['Dam2'])
        if a == 1:
            k = "Открыта"
        else:
            k = "Закрыта"
        return k

    def pump(self):
        a = self.__selectfrom(dist_table['Taldefax']['Pump']['Alarm'])
        if a == 1:
            k = "Авария"
        else:
            a = self.__selectfrom(dist_table['Taldefax']['Pump']['Status'])
            if a == 1:
                k = "Работа"
            else:
                k = "Остановлен"
        return k

    def compress1(self):
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress1']['Alarm'])
        if a == 1:
            k = "Авария"
        else:
            a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress1']['Status'])
            if a == 1:
                k = "Работа"
            else:
                k = "Остановлен"
        return k

    def compress2(self):
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress2']['Alarm'])
        if a == 1:
            k = "Авария"
        else:
            a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress2']['Status'])
            if a == 1:
                k = "Работа"
            else:
                k = "Остановлен"
        return k

    def compress3(self):
        a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress3']['Alarm'])
        if a == 1:
            k = "Авария"
        else:
            a = self.__selectfrom(dist_table['Taldefax']['Compress']['compress3']['Status'])
            if a == 1:
                k = "Работа"
            else:
                k = "Остановлен"
        return k

    def generator1(self):
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator1'])
        if a == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        return k

    def generator2(self):
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator2'])
        if a == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        return k

    def generator3(self):
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['generator3'])
        if a == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        return k

    def torch(self):
        a = self.__selectfrom(dist_table['Taldefax']['Machine']['torch'])
        if a == 1:
            k = "Авария Остановлен"
        else:
            k = "Работа Генерация"
        return k