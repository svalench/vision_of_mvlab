# Модуль настройки



## Данные о соединении от OPC

Отправить GET запрос на адрес
```
/dashboard/teldafax/connections/
```
После чего придет ответ со структурой
```
[
    {
        "connection_name": "connect1",
        "ip": "192.168.32.128"
    },
    {
        "connection_name": "s300_not_speed",
        "ip": "192.168.32.128"
    },
    {
        "connection_name": "plc1200_speed_data",
        "ip": "192.168.32.81"
    }
]
```

## Список переменных

Запрос **GET**  на адрес
```
dashboard/teldafax/connections/variables/<id>/
```
> id = порядковый номер соедиения в массиве
После чего придет ответ вида 
 ```
 [
    {
        "name": "vibro1"
    },
    ....
    {
        "name": "vibro2"
    }
 ]
 ```

## Статусы соединения

Необходимо отправить GET запрос на адрес
```/settings/status/connection/```
после чго будет получен ответ вида:
```
{
    <str:connection_name>: [
        <bool:status_connection>,
        <str:connection_name>,
        <str:ip_connection>
    ]
}
```
Если соединения нет будет приходить ответ вида:
```
{"error":[0,"error","no connection to socket"]}
```
## Wizard step1 и step2
```settings/wizard/step1```  
Ниже описана структура запроса POST для создания объекта на шагах wizard 1 и 2 
```
{
    name:<str>,
    customer:<str>,
    contract:<str>,
    structure:{
        levlel_<i>:<type>,
         ...
        levlel_<in>:<type>,
    }
}
```
где  
> Тип \<str> - строка длинной не более 255 символов
>
> \<type> ключ массива:  
>[0:'Резерв 1',1:'Резерв 2',2:'Организация',3:'Предприятие',4:'Завод',5:'Цех',6:'Узел',7:'Датчик']  
>[figma](https://www.figma.com/file/2ANgFF5NZFeAncpeTzJVvB/SystemOutForAll?node-id=222%3A1426)  
>\<i> - номер по порядку
## Получение данных о созданной структуре

```settings/wizard/step1```  
Данный GET запрос возвращает данные по созданной ранее структуре
```
{
    'name': <str>,
    'customer': <str>,
    'contract':<str>,
    'structure':{
        levlel_<i>:<type>,
         ...
        levlel_<in>:<type>,
    }
}
```
Описание переменных смотри выше  
в Случае отсутствия структуры придет  
```
{
    "result": "empty"
}
```
## Удаление структуры

Для удаления структуры необходимо отправить ***DELETE*** по адресу
```
settings/delete_structure
```
пОЛУЧИТЕ ОТВЕТ
```
{'result': 'structure <id> delete'}
```

## Создание цеха

Для добавления цеха необходимо передать на url
```
settings/create/department
```
POST запрос со следующим содержанием
```
{
    name:<str>,
    factory_id:<int>,
    shifts:[
        {
            start:<str:HH:MM:SS>
            end:<str:HH:MM:SS>
            lanch:[
                {
                    start:<str:HH:MM:SS>
                    end:<str:HH:MM:SS>
                },
                ....
            ]
        },
        ....
        
    ]
}
```