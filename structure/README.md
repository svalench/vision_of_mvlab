## Маршруты обращения
### */structure/*
Имеет метод GET.
Хранит информацию url адреса страниц: 
 «Corparation», «Factory», «Department», «Shift», «Lunch», «Agreagat», «Sensors», «ValueSensor»

### <a name="corp"> */structure/Corparation/* </a>
Хранит информацию о корпорациях(имя и т.д.). 
Имеет метод GET, POST.
Отображает поле:
* «id» - тип данных IntegerField
* «Name» - тип CharField
* «res2» - внешний ключ с таблицей «Reserv_2» 

Структура данных:
```
    {
        {
            "id": int,
            "name":str,
            "res2":<Query Object>
        },
        {
            -//-
        }, 
        .
        .
        .
    }
```

### <a name="fact"> */structure/Factory/* </a>
Хранит информацию о заводах. 
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «corp» - внешний ключ с таблицей [«Corparation»](#corp)
* «name» - тип CharField 
* «address» - тип CharField 

Структура данных:
```
    {
        {
            "id": int,
            "corp":<Query Object>,
            "name":str
        },
        {
            -//-
        },
        .
        .
        .
    }
```

### <a name="depa"> */structure/Department/* </a>
Хранит информацию об отделах.
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «factory» - внешний ключ с таблицей [«Factory»](#fact)
* «name» - тип CharField 

Структура данных:
```
    {
        {
            "id": int,
            "factory":<Query Object>,
            "name":str
        },
        {
            -//-
        },
        .
        .
        .
    }
```

### <a name="shif"> */structure/Shift/* </a>
Хранит информацию о сменах.
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «dep» - внешний ключ с таблицей [«Department»](#depa)
* «name» - тип CharField
* «start» - тип TimeField
* «end» - тип TimeField 

Структура данных:
```
    {
        {
            "id": int,
            "dep":<Query Object>,
            "name":str,
            "start":time,
            "end":time
        },
        {
            -//-
        },
        .
        .
        .
    }
```

### <a name="lunc"> */structure/Lunch/* </a>
Хранит информацию об обедах.
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «shift» - внешний ключ с таблицей [«Shift»](#shif)
* «name» - тип CharField
* «start» - тип TimeField
* «end» - тип TimeField 

Структура данных:
```
    {
        {
            "id": int,
            "shift":<Query Object>,
            "name":str,
            "start":time,
            "end":time
        },
        {
            -//-
        },
        .
        .
        .
    }
```

### <a name="agre"> */structure/Agreagat/* </a>
Хранит информацию об агрегатах.
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «dep» - внешний ключ с таблицей [«Department»](#depa)
* «name» - тип CharField 

Структура данных:
```
    {
        {
            "id":int,
            "dep":<Query Object>,
            "name":str
        },
        {
            -//-
        },
        .
        .
        .
    }
```

### <a name="sens"> */structure/Sensors/* </a>
Хранит информацию о датчиках.
Имеет метод GET, POST.
Отображает поля:
* «id» - тип данных IntegerField
* «agregat» - внешний ключ с таблицей [«Agreagat»](#agre)
* «name» - тип CharField
* «designation» - тип CharField 

Структура данных:
```
    {
        {
            "id":int,
            "agregat":<Query Object>,
            "name":str,
            "designation":str
        },
        {
            -//-
        },
        .
        .
        .
    }
```