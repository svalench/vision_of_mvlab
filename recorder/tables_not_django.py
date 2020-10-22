import json
from django.db import connection

class GetAllTable():
    """
    класс для получение списка таблиц которые не относятся к основной веб
    нужен для выбора табилц при привязке данных дачтикка к физическим данным модуля опроса
    где:
        _cursor - объкт драйвера подключения к БД
        engite - какая БД используется
    методы
        get_tables - возвращает все таблицы из БД которые не связаны с django
        get_tables_json - возвращает таблицы в json формате
    """
    def __init__(self):
        self._cursor = connection.cursor()
        self.engine = connection.vendor

    def get_tables(self):
        if(self.engine== 'sqlite'):
            self._cursor.execute("SELECT name FROM  sqlite_master WHERE type ='table' "
                                "AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'auth_%'"
                                "AND name NOT LIKE 'django_%' AND name NOT LIKE 'web_%';")
        elif(self.engine == 'postgresql'):
            self._cursor.execute("SELECT table_name FROM "
                            " information_schema.tables WHERE table_schema = 'public'  AND name NOT LIKE 'web_%'"
                            " AND name NOT LIKE 'auth_%' AND name NOT LIKE 'django_%' "
                            " ORDER BY table_name;")
        else:
            return 'error driver'
        result = self._cursor.fetchall()
        return result

    def get_tables_json(self):
        tables = self.get_tables()
        return json.dumps({'tables':tables})