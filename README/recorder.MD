# Документация API запросов для модуля Recorder  
## Создание, обновление, вывод и удаление рабочей области

**ВАЖНО!! Для получения данных необходимо в заголовке отправлять Token**  
> Header - Authorization: Token \<token>  

- Для создания нового рабочего пространства необходимо отправить ***POST*** запрос на сервер
по следующему пути
```
http(s)://<servername>/recorder/structure/Workspace/
```
> \/ в конце запросов обязателен
 
со следующими данными в теле:
```
{
    "name":<string>
}
```
> Имя может отсутствовать, в этом случае будет задано значение по умолчанию 
> \- workspace
- Для получения списка всех рабочих пространств пользователя необходимо
отправить ***GET*** запрос по адресу:
```
http(s)://<servername>/recorder/structure/Workspace/
```

После чего будет получен ответ вида:
```
[
    {
        "id": <int:id>,
        "child": [{"id":<int:id_workarea>},... ,{"id":<int:id_workarea>}],
        "name": <string:name>,
        "parent": <int:userid>
    },
    .....
    {
        "id": <int:id>,
        "child": [],
        "name": <string:name>,
        "parent": <int:userid>
    }
]
```

- <a name="href_to_workarea">Для получения одного рабочего пространства со списком вложенных рабочих областей
необходимо отправить ***GET*** запрос вида:</a>
```
http(s)://<servername>/recorder/structure/Workspace/<int:id>/
```
> id - идентификатор рабочего пространства

После чего будет получен ответ вида:
```

    {
        "id": <int:id>,
        "child": [{"id":<int:id_workarea>},... ,{"id":<int:id_workarea>}],
        "name": <string:name>,
        "parent": <int:userid>
    }

```

- Для обновления имени рабочего пространства необходимо отправить ***PUT*** запрос на адрес:
```
http(s)://<servername>/recorder/structure/Workspace/<id>/
```
> где \<id> - идентификатор рабочего пространства

с данными вида  
```
{
    "name":<str>
}
```
- Для удаления рабочего пространства необходимо отправить запрос ***DELETE*** на адресс:
```
http(s)://<servername>/recorder/structure/Workspace/<id>/
```
> где \<id> - идентификатор рабочего пространства


## Создание, обновление, вывод и удаление рабочей области  
##### *Чтобы получить "список графиков" смотри следующий подраздел*  

- Для создания рабочей области необходимо отправить ***POST*** запрос на адрес:
```
http(s)://<servername>/recorder/structure/Workarea/
```

с данными вида  

```
{
     "name":<string>,
     "parent":<int:id_workspace>,
     "data":[
                {"value":<int:id_valuesensor>,"color":<str:"#ffffff">},
                ....
                {"value":<int:id_valuesensor>,"color":<:str"#000fff">}
            ]
}
```
> data - обязательное поле может быть пустой массив   
> parent - обязательное поле не может быть пустым  
> data->value - обязательное поле
> date->color - необязательное поле значение по умолчанию - #000000

- Для получения списка **ВСЕХ** рабочих областей **ВСЕХ ПОЛЬЗОВАТЕЛЕЙ** необходимо отправить ***GET*** запрос на адрес:
```
http(s)://<servername>/recorder/structure/Workarea/
```
- Для получения рабочих областей определенной рабочей зоны необходимо отправить ***GET***
 запрос с параметром ```parent=<int:id>``` пример и описание ниже:
```
http(s)://<servername>/recorder/structure/Workarea/?parent=<int:id>
```
> где id - это идентификатор рабочей области
> здесь \/ в конце  ***ЗАПРЕЩЕН***  

- Для получения данных только одной рабочей области необходимо отправить ***GET*** запрос на адрес:

```
http(s)://<servername>/recorder/structure/Workarea/<int:id>/
```
> где id  - идентификатор рабочей области  

- Для обновления данных рабочей области необходимо отправить ***PUT*** запрос на адрес:  
```
http(s)://<servername>/recorder/structure/Workarea/<int:id>/
```
> где id  - идентификатор рабочей области  

С данными вида:  
```
{
     "name":<string>,
     "parent":<int:id_workspace>,
     "data":[
                {"value":<int:id_valuesensor>,"color":<str:"#ffffff">},
                ....
                {"value":<int:id_valuesensor>,"color":<:str"#000fff">}
            ]
}
```
> data - обязательное поле может быть пустой массив   
> parent - обязательное поле не может быть пустым  
> data->value - обязательное поле
> date->color - необязательное поле значение по умолчанию - #000000

- Для удаления рабочей области необходимо отправить запрос ***DELETE***  на адрес:  
```
http(s)://<servername>/recorder/structure/Workarea/<int:id>/
```

> где id  - идентификтор рабочей области  

## Получение списка графиков 
##### для выподающего списка в окне Работа с графиками: "Рабочая область N"


- Для получения списка графиков необходимо отправить запрос ***GET*** на адресс:
```
http(s)://<servername>/recorder/structure/ValueSensor/
```
> поле id этого запроса используется в создании рабочей области как id_valuesensor  

## Получение данных по рабочего пространства (с данными для графиков)

Для получения данных рабочей области необходимо отправить ***GET***  
 запрос по адресу:
 ```
http(s)://<servername>/recorder/chart/workarea/?id=<int:id>  
```
> id - идентификатор рабочей области список получаем [тут](#href_to_workarea)

После чего будет получен ответ вида:

```
{
    "id": <int:id>,
    "name": <string>,
    "parent": <int:id_workspace>,
    "child": [
        {
            "id": <int>,
            "workarea": <int>,
            "value": <int>,
            "color": <string>,
            "sensor_data": {
                "id": <int>,
                "sensor": <int>,
                "name": <string>,
                "name_connection": <string>,
                "table_name": <string>,
                "up_level_alarm": <real>,
                "down_level_alarm": <real>,
                "up_level": <real>,
                "down_level": <real>,
                "rate_change": <real>
            },
            "values": [{
                    "pk": <int>,
                    "now_time": <string:datetime>,
                    "value": <real>
                },
                ....
                {
                    "pk": <int>,
                    "now_time": <string:datetime>,
                    "value": <real>
                }]
        },
        ....
        {
            "id": <int>,
            "workarea": <int>,
            "value": <int>,
            "color": <string:color>,
            "sensor_data": {
                "id": <int>,
                "sensor": <int>,
                "name": <string:name>,
                "name_connection": <string:name_connection>,
                "table_name": <string:tablename>,
                "up_level_alarm": <real>,
                "down_level_alarm": <real>,
                "up_level": <real>,
                "down_level": <real>,
                "rate_change": <real>
            },
            "values": []
        }
    ]
}
```
> Если values = false  - ошибка запроса в БД

По умолчанию выводит данные за смену (если смены отсутсвуют выводит за день), для получения других данных смотри таблицу ниже:

| запрос                                                | период        | описание                          |
|-------------------------------------------------------|---------------|-----------------------------------|
|```/recorder/chart/workarea/?id=<int:id>&key=hour```   |   час         |Вернет данные за последний час     |
|```/recorder/chart/workarea/?id=<int:id>```            |   смена       |Вернет данные за последнию смену   |
|```/recorder/chart/workarea/?id=<int:id>&key=shift```  |
|```/recorder/chart/workarea/?id=<int:id>&key=day```    |   день        |Вернет данные за последний день    |
|```/recorder/chart/workarea/?id=<int:id>&key=week```   |   неделя      |Вернет данные за последнию неделю  |
|```/recorder/chart/workarea/?id=<int:id>&key=month```  |   месяц       |Вернет данные за последний месяц   |

Get data from to
```
http(s)://<servername>/recorder/chart/workarea/?id=<int:id_wirkarea>&start=<str:YYYY-MM-DD HH:mm:SS>&end=<str:YYYY-MM-DD HH:mm:SS>> 
```
returned period from start to end time. If value in period is None. Script will be return value by null
