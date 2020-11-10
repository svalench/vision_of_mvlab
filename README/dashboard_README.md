### */dashboard/duration/\<date>/day/*
Хранятся данные для виджета «Продолжительность работы, ч»,  для вкладки «сутки».

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/")  

Данные:
* "interval" - хранит массив объектов, которые состоят из:
   * "start" - тип данных time, время начала работы.
   * "end" - тип данных time, время конца работы.
   * "duration" - тип данных float, продолжительность в часах между "start" и end
* "sum" - тип данных float, суммарное время работы в часах.


```
{
    "interval":[
              {
                "start": time,
                "end": time,
                "duration": flot
              },
              .
              .
              .
    ],
    "sum": float
}
```


### */dashboard/duration/\<date>/shift/\<int:id>/*
Хранятся данные для виджета «Продолжительность работы, ч», с выбранной конкретной смены. 

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "interval" - хранит массив объектов, которые состоят из:
   * "start" - тип данных time, время начала работы.
   * "end" - тип данных time, время конца работы.
   * "duration" - тип данных float, продолжительность в часах между "start" и "end"
* "sum" - тип данных float, суммарное время работы в часах.


```
{
    "interval":[
              {
                "start": time,
                "end": time,
                "duration": flot
              },
              .
              .
              .
    ],
    "sum": float
}
```





### */dashboard/remainder/\<date>/*
Хранятся данные для виджета «Остатки на складах».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 


Данные:
* "storehouse" - массив объектов, которые состоят из:
  * "name" - тип данных str, хранит название склада
  * "iso" - массив из float, хранят численное значение остатков на складе.
  * "pol" - массив из float, хранят численное значение остатков на складе.
  * "pen" - массив из float, хранят численное значение остатков на складе.
* "in_total" - массив хранящий в себе следующие параметры:
  * "iso" - хранит float, суммарное значение по всем складам
  * "pol" - хранит float, суммарное значение по всем складам
  * "pen" - хранит float, суммарное значение по всем складам
```
{
	"storehouse":[
		{
                    "name":str,
                    "iso":[
                        float,
                        float,
                        .
                        .
                        .
                        ],
                    "pol":[
                        float,
                        float,
                        .
                        .
                        .
                        ],
                    "pen":[
                        float,
                        float,
                        .
                        .
                        .
                        ]
		},
		{
			-//-
		},
		.
		.
		.
	],
	"in_total":{
		"iso":float,
		"pol":float,
		"pen":float
	}
}
```

### */dashboard/edition/\<date>/month/*
Хранятся данные виджета «Выпуск панелей» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
 
Данные: 
* "suitable" - тип данных float, хранит значение поля "годно"
* "change_suitable" - тип данных float, хранит значение изменения в процентах
* "substandard" - тип данных float, хранит значение поля "некондиция"
* "change_substandard" - тип данных float, хранит значения изменения в процентах
* "defect" - тип данных float, хранит значение поля "брак"
* "change_defect" - тип данных float, хранит значение изменения в процентах
* "flooded" - тип данных float, хранит значение поля "залито метров"
* "change_flooded" - тип данных float, хранит значение изменения в процентах
* "sum" - тип данных float, хранит сумарное значение
* "change_sum" - тип данных float, хранит значение изменения в процентах
```
{
	"suitable":float,
	"change_suitable":float,
	"substandard":float,
	"change_substandard":float,
	"defect":float,
	"change_defect":float,
	"flooded":float,
	"change_flooded":float,
	"sum":float,
	"change_sum":float
}
```

### */dashboard/edition/\<date>/day/*
Хранятся данные виджета «Выпуск панелей» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 


Данные: 
* "suitable" - тип данных float, хранит значение поля "годно"
* "change_suitable" - тип данных float, хранит значение изменения в процентах
* "substandard" - тип данных float, хранит значение поля "некондиция"
* "change_substandard" - тип данных float, хранит значения изменения в процентах
* "defect" - тип данных float, хранит значение поля "брак"
* "change_defect" - тип данных float, хранит значение изменения в процентах
* "flooded" - тип данных float, хранит значение поля "залито метров"
* "change_flooded" - тип данных float, хранит значение изменения в процентах
* "sum" - тип данных float, хранит сумарное значение
* "change_sum" - тип данных float, хранит значение изменения в процентах
```
{
	"suitable":float,
	"change_suitable":float,
	"substandard":float,
	"change_substandard":float,
	"defect":float,
	"change_defect":float,
	"flooded":float,
	"change_flooded":float,
	"sum":float,
	"change_sum":float
}
```

### */dashboard/edition/\<date>/shift/\<int:id>/*
Хранятся данные виджета «Выпуск панелей» для вкладки «смена», с выбранной конкретной смены.

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные: 
* "suitable" - тип данных float, хранит значение поля "годно"
* "change_suitable" - тип данных float, хранит значение изменения в процентах
* "substandard" - тип данных float, хранит значение поля "некондиция"
* "change_substandard" - тип данных float, хранит значения изменения в процентах
* "defect" - тип данных float, хранит значение поля "брак"
* "change_defect" - тип данных float, хранит значение изменения в процентах
* "flooded" - тип данных float, хранит значение поля "залито метров"
* "change_flooded" - тип данных float, хранит значение изменения в процентах
* "sum" - тип данных float, хранит сумарное значение
* "change_sum" - тип данных float, хранит значение изменения в процентах
```
{
	"suitable":float,
	"change_suitable":float,
	"substandard":float,
	"change_substandard":float,
	"defect":float,
	"change_defect":float,
	"flooded":float,
        "change_flooded":float,
	"sum":float,
	"change_sum":float
}
```

### */dashboard/sumexpense/\<date>/month/*
Хранятся данные виджета «Суммарный расход» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/")  

Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```



### */dashboard/sumexpense/\<date>/day/*
Хранятся данные виджета «Суммарный расход» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 


Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```

### */dashboard/sumexpense/\<date>/shift/\<int:id>/*
Хранятся данные виджета «Суммарный расход» для вкладки «смена», с выбранной конкретной смены.  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```

### */dashboard/energyconsumption/\<date>/month/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "input1" - тип данных float, хранит значение поля "Ввод1, кВт"
* "input2" - тип данных float, хранит значение поля "Ввод2, кВт"
* "gas" - тип данных float, хранит значение поля "Газ, м3"
```
{
	"input1":float,
	"input2":float,
	"gas":float
}
```


### */dashboard/energyconsumption/\<date>/day/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "input1" - тип данных float, хранит значение поля "Ввод1, кВт"
* "input2" - тип данных float, хранит значение поля "Ввод2, кВт"
* "gas" - тип данных float, хранит значение поля "Газ, м3"
```
{
	"input1":float,
	"input2":float,
	"gas":float
}
```

### */dashboard/energyconsumption/\<date>/shift/\<int:id>/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «смена», с выбранной конкретной смены.  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "input1" - тип данных float, хранит значение поля "Ввод1, кВт"
* "input2" - тип данных float, хранит значение поля "Ввод2, кВт"
* "gas" - тип данных float, хранит значение поля "Газ, м3"
```
{
	"input1":float,
	"input2":float,
	"gas":float
}
```

### */dashboard/specificconsumption/\<date>/month/*
Хранятся данные виджета «Удельный расход на км» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```


### */dashboard/specificconsumption/\<date>/day/*
Хранятся данные виджета «Удельный расход на км» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```


### */dashboard/specificconsumption/\<date>/shift/\<int:id>/*
Хранятся данные виджета «Удельный расход на км» для вкладки «смена», с выбранной конкретной смены.  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "iso" - тип данных float
* "pol" - тип данных float
* "pen" - тип данных float
* "kat1" - тип данных float
* "kat2" - тип данных float
* "kat3" - тип данных float
```
{
	"iso":float,
	"pol":float,
	"pen":float,
	"kat1":float,
	"kat2":float,
	"kat3":float
}
```




### */dashboard/comparison/month/\<date1>/\<date2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «месяц».  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
  
  
Данные:
* "suitable1" - тип данных float, хранит значение поля "годно" для "date1"
* "suitable2" - тип данных float, хранит значение поля "годно" для "date2"
* "substandard1" - тип данных float, хранит значение поля "некондиция"для "date1"
* "substandard2" - тип данных float, хранит значение поля "некондиция"для "date2"
* "defect1" - тип данных float, хранит значение поля "брак"для "date1"
* "defect2" - тип данных float, хранит значение поля "брак"для "date2"
* "flooded1" - тип данных float, хранит значение поля "залито метров"для "date1"
* "flooded2" - тип данных float, хранит значение поля "залито метров"для "date2"
* "sum1" - тип данных float, хранит сумарное значениедля "date1"
* "sum2" - тип данных float, хранит сумарное значениедля "date2"
```
{
	"suitable1":float,
	"suitable2":float,
	"substandard1":float,
	"substandard2":float,
	"defect1":float,
	"defect2":float,
	"flooded1":float,
	"flooded2":float,
	"sum1":float,
	"sum2":float
}
```


### */dashboard/comparison/day/\<date1>/\<date2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «сутки».  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), первой половины
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), второй половины

Данные:
* "suitable1" - тип данных float, хранит значение поля "годно" для "date1"
* "suitable2" - тип данных float, хранит значение поля "годно" для "date2"
* "substandard1" - тип данных float, хранит значение поля "некондиция"для "date1"
* "substandard2" - тип данных float, хранит значение поля "некондиция"для "date2"
* "defect1" - тип данных float, хранит значение поля "брак"для "date1"
* "defect2" - тип данных float, хранит значение поля "брак"для "date2"
* "flooded1" - тип данных float, хранит значение поля "залито метров"для "date1"
* "flooded2" - тип данных float, хранит значение поля "залито метров"для "date2"
* "sum1" - тип данных float, хранит сумарное значениедля "date1"
* "sum2" - тип данных float, хранит сумарное значениедля "date2"
```
{
	"suitable1":float,
	"suitable2":float,
	"substandard1":float,
	"substandard2":float,
	"defect1":float,
	"defect2":float,
	"flooded1":float,
	"flooded2":float,
	"sum1":float,
	"sum2":float
}
```


### */dashboard/comparison/shift/\<date1>/\<int:id1>/\<date2>/\<int:id2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «смена», с выбранными конкретными сменами.  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), первой половины 
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), второй половины 
* \<int:id1> - номер смены первой половины
* \<int:id2> - номер смены второй половины

Данные:
* "suitable1" - тип данных float, хранит значение поля "годно" для "date1"
* "suitable2" - тип данных float, хранит значение поля "годно" для "date2"
* "substandard1" - тип данных float, хранит значение поля "некондиция"для "date1"
* "substandard2" - тип данных float, хранит значение поля "некондиция"для "date2"
* "defect1" - тип данных float, хранит значение поля "брак"для "date1"
* "defect2" - тип данных float, хранит значение поля "брак"для "date2"
* "flooded1" - тип данных float, хранит значение поля "залито метров"для "date1"
* "flooded2" - тип данных float, хранит значение поля "залито метров"для "date2"
* "sum1" - тип данных float, хранит сумарное значениедля "date1"
* "sum2" - тип данных float, хранит сумарное значениедля "date2"
```
{
	"suitable1":float,
	"suitable2":float,
	"substandard1":float,
	"substandard2":float,
	"defect1":float,
	"defect2":float,
	"flooded1":float,
	"flooded2":float,
	"sum1":float,
	"sum2":float
}
```