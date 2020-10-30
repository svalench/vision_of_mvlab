### */dashboard/prodrab/\<date>/*
Хранятся данные для виджета «Продолжительность работы, ч». 

Данные в маршруте:
* \<date> - дата имеет вид ""
Данные ответа:
* "otr_vrem" - хранит масив объектов, которые состоят из:
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
```
{
	"godno":int,
	"prir_godno":int,
	"nekondiciya":int,
	"prir_nekondiciya":int,
	"brak":int,
	"prir_brak":int,
	"zalito":int,
	"prir_zalito":int,
	"summa":int,
	"prir_summa":int
}
```

### */dashboard/vipusk/\<date>/smena/\<int:id>/*
Хранятся данные виджета «Выпуск панелей» для вкладки «смена», с выбранной конкретной смены.
```
{
	"godno":int,
	"prir_godno":int,
	"nekondiciya":int,
	"prir_nekondiciya":int,
	"brak":int,
	"prir_brak":int,
	"zalito":int,
	"summa":int,
	"prir_summa":int
}
```

### */dashboard/sumar_rashod/\<date>/mesyac/*
Хранятся данные виджета «Суммарный расход» для вкладки «месяц».
```
{
	"iso":int,
	"pol":int,
	"pen":int,
	"kat1":int,
	"kat2":int,
	"kat3":int
}
```



### */dashboard/sumar_rashod/\<date>/cutki/*
Хранятся данные виджета «Суммарный расход» для вкладки «сутки».
```
{
	"iso":int,
	"pol":int,
	"pen":int,
	"kat1":int,
	"kat2":int,
	"kat3":int
}
```

### */dashboard/sumar_rashod/\<date>/smena/\<int:id>/*
Хранятся данные виджета «Суммарный расход» для вкладки «смена», с выбранной конкретной смены.
```
{
	"iso":int,
	"pol":int,
	"pen":int,
	"kat1":int,
	"kat2":int,
	"kat3":int
}
```

### */dashboard/rashod_energores/\<date>/mesyac/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «месяц».
```
{
	"vvod1":int,
	"vvod2":int,
	"gaz":int
}
```


### */dashboard/rashod_energores/\<date>/cutki/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «сутки».
```
{
	"vvod1":int,
	"vvod2":int,
	"gaz":int
}
```

### */dashboard/rashod_energores/\<date>/smena/\<int:id>/*
Хранятся данные виджета «Расход энергоресурсов» для вкладки «смена», с выбранной конкретной смены.
```
{
	"vvod1":int,
	"vvod2":int,
	"gaz":int
}
```

### */dashboard/ydel_rashod/\<date>/mesyac/*
Хранятся данные виджета «Удельный расход на км» для вкладки «месяц».
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




### */dashboard/modul_sravn/mesyac/\<data>/\<data>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «месяц».
```
{
	"godno1":int,
	"godno2":int,
	"nekondiciya1":int,
	"nekondiciya2":int,
	"brak1":int,
	"brak2":int,
	"zalito1":int,
	"zalito2":int,
	"summa1":int,
	"summa2":int
}
```


### */dashboard/modul_sravn/cutki/\<data>/\<data>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «сутки».
```
{
	"godno1":int,
	"godno2":int,
	"nekondiciya1":int,
	"nekondiciya2":int,
	"brak1":int,
	"brak2":int,
	"zalito1":int,
	"zalito2":int,
	"summa1":int,
	"summa2":int
}
```


### */dashboard/modul_sravn/smena/\<date>/\<int:id>/\<date>/\<int:id>/*
Хранятся данные виджета «Модуль сравнения» для вкладки «смена», с выбранными конкретными сменами.
```
{
	"godno1":int,
	"godno2":int,
	"nekondiciya1":int,
	"nekondiciya2":int,
	"brak1":int,
	"brak2":int,
	"zalito1":int,
	"zalito2":int,
	"summa1":int,
	"summa2":int

}
```