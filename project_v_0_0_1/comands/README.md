# Команды для нормального запуска проекта

```python3 -m venv venv```

- [x] создание окружения
- [ ] установка зависимостей
- [ ] провести миграции
- [ ] произвести создание начальной структуры

```pip3 install -r requiremens.txt```

- [x] создание окружения
- [x] установка зависимостей
- [ ] провести миграции
- [ ] произвести создание начальной структуры

>Перед тем как провести миграции необходимо настроить подключение к БД

```python3 manage.py makemigrations```  
```python3 manage.py migrate```

- [x] создание окружения
- [x] установка зависимостей
- [x] провести миграции
- [ ] произвести создание начальной структуры

<a name="comands_create_models">```python3 manage.py add_reserv <name1> <name2>```</a>
> описание команды смотри [здесь](/structure/management/README.md)
- [x] создание окружения
- [x] установка зависимостей
- [x] провести миграции
- [x] произвести создание начальной структуры