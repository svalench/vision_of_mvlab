### */dashboard/prodrab/\<date>/mesyac/*
Хранятся данные для виджета «Продолжительность работы, ч», для вкладки «месяц». 

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/")   

Данные:
* "otr_vrem" - хранит массив объектов, которые состоят из:
   * "nach_rab" - тип данных time, время начала работы.
   * "kon_rab" - тип данных time, время конца работы.
   * "prodolg" - тип данных float, продолжительность в часах между "nach_rab" и kon_rab
* "sumar_vrem" - тип данных float, суммарное время работы в часах.


```
{
    "otr_vrem":[
              {
                "nach_rab": time,
                "kon_rab": time,
                "prodolg": flot
              },
              .
              .
              .
    ],
    "sumar_vrem": float
}
```

### */dashboard/prodrab/\<date>/cutki/*
Хранятся данные для виджета «Продолжительность работы, ч»,  для вкладки «сутки».

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
Данные:
* "otr_vrem" - хранит массив объектов, которые состоят из:
   * "nach_rab" - тип данных time, время начала работы.
   * "kon_rab" - тип данных time, время конца работы.
   * "prodolg" - тип данных float, продолжительность в часах между "nach_rab" и kon_rab
* "sumar_vrem" - тип данных float, суммарное время работы в часах.


```
{
    "otr_vrem":[
              {
                "nach_rab": time,
                "kon_rab": time,
                "prodolg": flot
              },
              .
              .
              .
    ],
    "sumar_vrem": float
}
```


### */dashboard/vipusk/\<date>/smena/\<int:id>/*
Хранятся данные для виджета «Продолжительность работы, ч», с выбранной конкретной смены. 

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "otr_vrem" - хранит массив объектов, которые состоят из:
   * "nach_rab" - тип данных time, время начала работы.
   * "kon_rab" - тип данных time, время конца работы.
   * "prodolg" - тип данных float, продолжительность в часах между "nach_rab" и kon_rab
* "sumar_vrem" - тип данных float, суммарное время работы в часах.


```
{
    "otr_vrem":[
              {
                "nach_rab": time,
                "kon_rab": time,
                "prodolg": flot
              },
              .
              .
              .
    ],
    "sumar_vrem": float
}
```





### */dashboard/ostat/\<date>/*
Хранятся данные для виджета «Остатки на складах».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 


Данные:
* "sklad" - массив объектов, которые состоят из:
  * "name" - тип данных str, хранит название склада
  * "iso" - массив из float, хранят численное значение остатков на складе.
  * "pol" - массив из float, хранят численное значение остатков
  * "pen" - массив из float, хранят численное значение остатков
* "itog" - массив хранящий в себе следующие параметры:
  * "iso" - хранит float, сумарное значение по всем складам
  * "pol" - хранит float, сумарное значение по всем складам
  * "pen" - хранит float, сумарное значение по всем складам
```
{
	"sklad":[
		{
                    "name":str,
                    "iso":{
                        float,
                        float,
                        .
                        .
                        .
                        },
                    "pol":{
                        float,
                        float,
                        .
                        .
                        .
                        },
                    "pen":{
                        float,
                        float,
                        .
                        .
                        .
                        },
		},
		{
			-//-
		},
		.
		.
		.
	],
	"itog":{
		"iso":float,
		"pol":float,
		"pen":float
	}
}
```

### */dashboard/vipusk/\<date>/mesyac/*
Хранятся данные виджета «Выпуск панелей» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
 
Данные: 
* "godno" - тип данных float
* "prir_godno" - тип данных float
* "nekondiciya" - тип данных float
* "prir_nekondiciya" - тип данных float
* "brak" - тип данных float
* "prir_brak" - тип данных float
* "zalito" - тип данных float
* "prir_zalito" - тип данных float
* "summa" - тип данных float
* "prir_summa" - тип данных float
```
{
	"godno":float,
	"prir_godno":float,
	"nekondiciya":float,
	"prir_nekondiciya":float,
	"brak":float,
	"prir_brak":float,
	"zalito":float,
	"prir_zalito":float,
	"summa":float,
	"prir_summa":float
}
```

### */dashboard/vipusk/\<date>/cutki/*
Хранятся данные виджета «Выпуск панелей» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 


Данные:
* "godno" - тип данных float
* "prir_godno" - тип данных float
* "nekondiciya" - тип данных float
* "prir_nekondiciya" - тип данных float
* "brak" - тип данных float
* "prir_brak" - тип данных float
* "zalito" - тип данных float
* "prir_zalito" - тип данных float
* "summa" - тип данных float
* "prir_summa" - тип данных float
```
{
	"godno":float,
	"prir_godno":float,
	"nekondiciya":float,
	"prir_nekondiciya":float,
	"brak":float,
	"prir_brak":float,
	"zalito":float,
	"prir_zalito":float,
	"summa":float,
	"prir_summa":float
}
```

### */dashboard/vipusk/\<date>/smena/\<int:id>/*
Хранятся данные виджета «Выпуск панелей» для вкладки «смена», с выбранной конкретной смены.

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "godno" - тип данных float
* "prir_godno" - тип данных float
* "nekondiciya" - тип данных float
* "prir_nekondiciya" - тип данных float
* "brak" - тип данных float
* "prir_brak" - тип данных float
* "zalito" - тип данных float
* "prir_zalito" - тип данных float
* "summa" - тип данных float
* "prir_summa" - тип данных float
```
{
	"godno":float,
	"prir_godno":float,
	"nekondiciya":float,
	"prir_nekondiciya":float,
	"brak":float,
	"prir_brak":float,
	"zalito":float,
	"summa":float,
	"prir_summa":float
}
```

### */dashboard/sumar_rashod/\<date>/mesyac/*
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



### */dashboard/sumar_rashod/\<date>/cutki/*
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

### */dashboard/sumar_rashod/\<date>/smena/\<int:id>/*
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

### */dashboard/rashod_energores/\<date>/mesyac/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «месяц».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "vvod1" - тип данных float
* "vvod2" - тип данных float
* "gaz" - тип данных float
```
{
	"vvod1":float,
	"vvod2":float,
	"gaz":float
}
```


### */dashboard/rashod_energores/\<date>/cutki/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «сутки».  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 

Данные:
* "vvod1" - тип данных float
* "vvod2" - тип данных float
* "gaz" - тип данных float
```
{
	"vvod1":float,
	"vvod2":float,
	"gaz":float
}
```

### */dashboard/rashod_energores/\<date>/smena/\<int:id>/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «смена», с выбранной конкретной смены.  

Данные в маршруте:
* \<date> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<int:id> - номер смены ("/1/")  

Данные:
* "vvod1" - тип данных float
* "vvod2" - тип данных float
* "gaz" - тип данных float
```
{
	"vvod1":float,
	"vvod2":float,
	"gaz":float
}
```

### */dashboard/ydel_rashod/\<date>/mesyac/*
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


### */dashboard/ydel_rashod/\<date>/cutki/*
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


### */dashboard/ydel_rashod/\<date>/smena/\<int:id>/*
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




### */dashboard/modul_sravn/mesyac/\<date1>/\<date2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «месяц».  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/") 
  
Данные:
* "godno1" - тип данных float
* "godno2" - тип данных float
* "nekondiciya1" - тип данных float
* "nekondiciya2" - тип данных float
* "brak1" - тип данных float
* "brak2" - тип данных float
* "zalito1" - тип данных float
* "zalito2" - тип данных float
* "summa1" - тип данных float
* "summa2" - тип данных float
```
{
	"godno1":float,
	"godno2":float,
	"nekondiciya1":float,
	"nekondiciya2":float,
	"brak1":float,
	"brak2":float,
	"zalito1":float,
	"zalito2":float,
	"summa1":float,
	"summa2":float
}
```


### */dashboard/modul_sravn/cutki/\<date1>/\<date2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «сутки».  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), первой половины
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), второй половины

Данные:
* "godno1" - тип данных float
* "godno2" - тип данных float
* "nekondiciya1" - тип данных float
* "nekondiciya2" - тип данных float
* "brak1" - тип данных float
* "brak2" - тип данных float
* "zalito1" - тип данных float
* "zalito2" - тип данных float
* "summa1" - тип данных float
* "summa2" - тип данных float
```
{
	"godno1":float,
	"godno2":float,
	"nekondiciya1":float,
	"nekondiciya2":float,
	"brak1":float,
	"brak2":float,
	"zalito1":float,
	"zalito2":float,
	"summa1":float,
	"summa2":float
}
```


### */dashboard/modul_sravn/smena/\<date1>/\<int:id1>/\<date2>/\<int:id2>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «смена», с выбранными конкретными сменами.  

Данные в маршруте:
* \<date1> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), первой половины 
* \<date2> - дата имеет вид гггг-мм-дд ("/2011-02-12/"), второй половины 
* \<int:id1> - намер смены первой половины
* \<int:id2> - намер смены второй половины

Данные:
* "godno1" - тип данных float
* "godno2" - тип данных float
* "nekondiciya1" - тип данных float
* "nekondiciya2" - тип данных float
* "brak1" - тип данных float
* "brak2" - тип данных float
* "zalito1" - тип данных float
* "zalito2" - тип данных float
* "summa1" - тип данных float
* "summa2" - тип данных float
```
{
	"godno1":float,
	"godno2":float,
	"nekondiciya1":float,
	"nekondiciya2":float,
	"brak1":float,
	"brak2":float,
	"zalito1":float,
	"zalito2":float,
	"summa1":float,
	"summa2":float

}
```