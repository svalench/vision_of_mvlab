# Описание запросов для вкладки Recorder -> Variables  

ДЛя получение списка всех переменных необходимо отправить **GET** запрос на адресс:
```
http(s)://<servername>/recorder/structure/ValueSensor/
```
  
После чего придет ответ вида:  
  
```
[
    {
        "id": <int>,
        "sensor_name": <str>,
        "uzel_name": <str>,
        "department_name": <str>,
        "name": <str>,
        "name_connection": <str>,
        "table_name": <str>,
        "up_level_alarm": <float>,
        "down_level_alarm": <float>,
        "up_level": <float>,
        "down_level": <float>,
        "rate_change": <float>,
        "sensor": <int>
    },
    ....
    {
        "id": <int>,
        "sensor_name": <str>,
        "uzel_name": <str>,
        "department_name": <str>,
        "name": <str>,
        "name_connection": <str>,
        "table_name": <str>,
        "up_level_alarm": <float>,
        "down_level_alarm": <float>,
        "up_level": <float>,
        "down_level": <float>,
        "rate_change": <float>,
        "sensor": <int>
    }
]
```

ДЛя добавления наого значени необходимо отправить запос **POST** на адрес:

```
http(s)://<servername>/recorder/structure/ValueSensor/
```
с данными вида

```
{
        "name": <str>*,
        "name_connection": <str>*,
        "table_name": <str:tablename>,
        "up_level_alarm": <real>*,
        "down_level_alarm": <real>*,
        "up_level": <real>*,
        "down_level": <real>*,
        "rate_change": <real>*,
        "sensor": <id:parent_sensorId>
}
```
>  "*" \- необязательные параметры  
  
Для получение данных одной переменной необходимо отправить **GET** запрос на адрес
```
http(s)://<servername>/recorder/structure/ValueSensor/<int:id>/
```

и получим данные вида 

```
    {
        "id": <int>,
        "sensor_name": <str>,
        "uzel_name": <str>,
        "department_name": <str>,
        "name": <str>,
        "name_connection": <str>,
        "table_name": <str>,
        "up_level_alarm": <float>,
        "down_level_alarm": <float>,
        "up_level": <float>,
        "down_level": <float>,
        "rate_change": <float>,
        "sensor": <int>
    }

```

Для обновления данных необходимо отправить **PUT** запрос на адрес:  
```
http(s)://<servername>/recorder/structure/ValueSensor/<int:id>/
```
с данными вида

```
{
        "name": <str>*,
        "name_connection": <str>*,
        "table_name": <str:tablename>,
        "up_level_alarm": <real>*,
        "down_level_alarm": <real>*,
        "up_level": <real>*,
        "down_level": <real>*,
        "rate_change": <real>*,
        "sensor": <id:parent_sensorId>
}
```
>  "*" \- необязательные параметры  