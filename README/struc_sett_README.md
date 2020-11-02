### *Вкладка резерв 1*
POST запрос.  
Путь: /structure/Reserv1/  
```
{
    "name":str
}
```

### *Вкладка резерв 2*

GET запрос.
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```

POST запрос.  
Путь: /structure/Reserv1/  
```
{
    "name":str,
    "res1":int(id)
}
```

### *Вкладка Организация*
GET запрос.
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```

GET запрос.
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```

POST запрос.  
Путь: /structure/Corparation/
```
{
    "name":str,
    "res1":int(id)
}
```

### *Вкладка Предприятие*
GET запрос.  
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```
GET запрос.  
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Corparation/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "res2":int(id)
    },
    ...
}
```
POST запрос.  
Путь: /structure/Company/
```
{
    "name":str,
    "corp":int(id)
}
```

### *Вкладка Завод*
GET запрос.  
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```
GET запрос.  
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Corparation/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "res2":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Company/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "corp":int(id)
    },
    ...
}
```
POST запрос.  
Путь: /structure/Factory/
```
{
    "comp":int(id),
    "name":str,
    "address":str
}
```


### *Вкладка Цех*

GET запрос.  
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```
GET запрос.  
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Corparation/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "res2":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Company/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "corp":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Factory/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "comp":int(id),
        "address":str
    },
    ...
}
```
POST запрос.  
Путь: /structure/Department/
```
{
    name:str,
    factory:int(id),
    shifts:[
        {
            start:str(HH:MM:SS)
            end:str(HH:MM:SS)
            lanch:[
                {
                    start:str(HH:MM:SS)
                    end:str(HH:MM:SS)
                },
                ....
            ]
        },
        ....
        
    ]
}
```

### *Вкладка Цех*

GET запрос.  
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```
GET запрос.  
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Corparation/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "res2":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Company/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "corp":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Factory/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "comp":int(id),
        "address":str
    },
    ...
}
```

GET запрос.  
Путь: /settings/Department/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "factory":int(id)
    },
    ...
}
```
POST запрос.  
Путь: /structure/Agreagat/
```
{
    "name":str,
    "dep":int(id)
}
```

### *Вкладка Датчик*

GET запрос.  
Путь: /structure/Reserv1/
```
{
    {
        "id":int,
        "name":str
    },
    ...
}
```
GET запрос.  
Путь: /settings/Reserv2/search/\<int:pk>/
```
{
    {
        "id":int,
        "name":str,
        "res1":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Corparation/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "res2":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Company/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "corp":int(id)
    },
    ...
}
```
GET запрос.  
Путь: /settings/Factory/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "comp":int(id),
        "address":str
    },
    ...
}
```

GET запрос.  
Путь: /settings/Department/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "factory":int(id)
    },
    ...
}
```

GET запрос.  
Путь: /settings/Agreagat/search/\<int:id>/
```
{
    {
        "id":int,
        "name":str,
        "dep":int(id)
    },
    ...
}
```
POST запрос.  
Путь: /structure/Sensors/
```
{
    "agregat":int(id),
    "name":str,
    "designation":str
}
```
