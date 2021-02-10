## ***Получение доступных виджетов пользователя***
Адрес GET запроса:  
**"host"/dashboard/user/**  
Ответ имеет вид:
```
[
    str,
    str,
    str,
    str,
    str,
    str
]
```
Пояснение:
[0:"DurationIntervalDay",1:"Storehouse",2:"EditionDay",3:"SumexpenseDay",4:"EnergyConsumptionDay",5:"SpecificConsumptionDay"]  
0:"DurationIntervalDay" --> Виджет «Продолжительность работы, ч»  
1:"Storehouse" --> Виджет «Остатки на складах»  
2:"EditionDay" --> Виджет «Выпуск панелей»  
3:"SumexpenseDay" --> Виджет «Суммарный расход»  
4:"EnergyConsumptionDay" --> Виджет «Расход энергоресурсов»  
5:"SpecificConsumptionDay" --> Виджет «Удельный расход на км»

В случае когда у пользователя нет доступа к виджету, на его месте будет значение null. Пример ответа:
```
[
    "DurationIntervalDay",
    "Storehouse",
    "EditionDay",
    null,
    null,
    "SpecificConsumptionDay"
]
```
