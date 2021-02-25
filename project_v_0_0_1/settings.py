"""
Django settings for project_v_0_0_1 project.

CORS_ALLOW_ALL_ORIGINS = True
=======

def get_env_value(env_variable, for_develop):
    try:
        return os.environ[env_variable]
    except:
        return for_develop


SECRET_KEY = '+h4b@t!%)**n@v6#o4o$x9tme_!8ju%62l4gqpk^7+xf_$#2_5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_value('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition
# sdcfs
INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'drf_generators',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'structure',
    'users',
    'recorder',
    'dashboard',

    'finalware',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_v_0_0_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_v_0_0_1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': get_env_value('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': get_env_value('DB_NAME', str(BASE_DIR / 'dbs1213.sqlite3')),
        'USER': get_env_value('DB_USER', ''),
        'PASSWORD': get_env_value('DB_PASSWORD', ''),
        'HOST': get_env_value('DB_HOST', ''),
        'PORT': get_env_value('DB_PORT', ''),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'db1',
    #     'USER': 'lex',
    #     'PASSWORD': '123',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
}

SITE_SUPERUSER_USERNAME = get_env_value('SUPERUSER_NAME', 'wert')

# This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = get_env_value('SUPERUSER_EMAIL', 'av@mvlab.by')

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = get_env_value('SUPERUSER_PASSWORD', '123')


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.BasePermission',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

}

CORS_ALLOWED_ORIGINS = [
    "http://mvlab.devzsg.net",
    "http://localhost:8000",
]

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.UserP'
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BASE_STRUCTURE = (
    'Reserv_1', 'Reserv_2', 'Corparation', 'Company', 'Factory', 'Department', 'Agreagat', 'Sensors')
SOCKET_PORT_SEREVER = get_env_value('SOCKET_PORT', 8086)

'''
dist_table:
    "EditionDay" - хранится имя таблицы, вне django, с данными для виджета "Выпуск панелей"
    "SumexpenseDay" - словарь хронящий перечень расходуемых веществ для виджета "Суммарный расход":
        "iso" - хранятся имена таблиц с данными по Изоцианату
        "pol" - хранятся имена таблиц с данными по Полиолу
        "pen" - хранятся имена таблиц с данными по Пентану
        "kat1" - хранятся имена таблиц с данными по Катализатору 1
        "kat2" - хранятся имена таблиц с данными по Катализатору 1
        "kat3" - хранятся имена таблиц с данными по Катализатору 1
    "EnergyConsumptionDay" - словарь с перечнем энерго ресурсов для виджета "Расход энергоресурсов":
        "input1" - хранит имя таблицы с данными по Вводу 1
        "input2" - хранит имя таблицы с данными по Вводу 2
        "gas" - хранит имя таблицы с данными по Газу
    "SpecificConsumptionDay" - словарь хронящий перечень расходуемых веществ для виджета "Удельный расход на км":
        "iso" - хранятся имена таблиц с данными по Изоцианату
        "pol" - хранятся имена таблиц с данными по Полиолу
        "pen" - хранятся имена таблиц с данными по Пентану
        "kat1" - хранятся имена таблиц с данными по Катализатору 1
        "kat2" - хранятся имена таблиц с данными по Катализатору 1
        "kat3" - хранятся имена таблиц с данными по Катализатору 1
    "Taldefax" - словарь хронящий перечень виджитов для Taldefax:
        "TransitionReadings" - словарь хронящий перечень имена таблиц для виджета "Показания перехода":
            "methane" - хранит имя таблицы по метану
            "сarbon dioxide" - хранит имя таблицы по углекислому газу
            "oxygen" - хранит имя таблицы по кислороду
            "pressure in" - хранит имя таблицы по Давлению (вх.генер.)
            "pressure out" - хранит имя таблицы по Давлению (вых.компар.)
            "consumption" - хранит имя таблицы по расходу
            "temperature" - хранит имя таблицы по температуре
        "GenerationOfElectricity" - словарь хронящий перечень имен таблиц для виджета "Выработка электроэнергии":
            "machine 1" - хранит имя таблицы для мощности машины 1
            "machine 2" - хранит имя таблицы для мощности машины 2
            "machine 3" - хранит имя таблицы для мощности машины 3
            "machine 4" - хранит имя таблицы для мощности машины 4
        "Mode" - хранит имя таблицы для виджета "Режим работы"
        "Damper" - словарь хронящий перечень имен таблиц для виджета "Задвижки":
            "Dam1" - хранит имя таблицы для положения задвижки 1
            "Dam2" - хранит имя таблицы для положения задвижки 2
        "Pump" - словарь хронящий перечень имен таблиц для виджета "Насосы":
            "Status" - хранит имя таблицы для статуса насоса
            "Alarm" - хранит имя таблицы для аварии насоса
        "Compress" - словарь хронящий инфорамцию для виджета "Компрессоры":
            "compress1" - словарь хронящий перечень имен таблиц для компрессора 1:
                "Status" - хранит имя таблицы для статуса компрессора
                "Alarm" - хранит имя таблицы для аварии компрессора
            "compress2" - словарь хронящий перечень имен таблиц для компрессора 2:
                "Status" - хранит имя таблицы для статуса компрессора
                "Alarm" - хранит имя таблицы для аварии компрессора
            "compress3" - словарь хронящий перечень имен таблиц для компрессора 3:
                "Status" - хранит имя таблицы для статуса компрессора
                "Alarm" - хранит имя таблицы для аварии компрессора
        "Machine" - словарь хронящий перечень имен таблиц для виджета "Машины":
            "generator1" - хранит имя таблицы для статуса генератора 1
            "generator2" - хранит имя таблицы для статуса генератора 2
            "generator3" - хранит имя таблицы для статуса генератора 3
            "generator4" - хранит имя таблицы для статуса генератора 4
            "torch" - хранит имя таблицы для статуса факела
'''
dist_table = {
    "DurationIntervalDay": ["m_fosd", 1],
    "EditionDay": "Edition",
    "SumexpenseDay": {
        "iso": ['iso0', 'iso2'],
        "pol": ['pol1', 'pol2'],
        "pen": ['pen1', 'pen2'],
        "kat1": ['kat1'],
        "kat2": ['kat2'],
        "kat3": ['kat3']
    },
    "EnergyConsumptionDay": {
        "input1": "in1",
        "input2": "in2",
        "gas": "gas1"
    },
    "SpecificConsumptionDay": {
        "iso": ['iso0', 'iso2'],
        "pol": ['pol1', 'pol2'],
        "pen": ['pen1', 'pen2'],
        "kat1": ['kat1'],
        "kat2": ['kat2'],
        "kat3": ['kat3']
    },
    "Taldefax": {
        "TransitionReadings": {
            "methane": "mvlab_temp_real_1",
            "сarbon dioxide": "mvlab_temp_real_2",
            "oxygen": "mvlab_temp_real_3",
            "pressure in": "mvlab_temp_real_4",
            "pressure out": "mvlab_temp_real_5",
            "consumption": "mvlab_temp_real_6",
            "temperature": "mvlab_temp_real_1"
        },
        "GenerationOfElectricity": {
            "machine 1": "mvlab_temp_real_1",
            "machine 2": "mvlab_temp_real_2",
            "machine 3": "mvlab_temp_real_3",
            "machine 4": "mvlab_temp_real_4"
        },
        "Mode": "m_true",
        "Damper": {
            "Dam1": "m_true",
            "Dam2": "m_true"
        },
        "Pump": {
            "Status": "m_true",
            "Alarm": "m_fo"
        },
        "Compress": {
            "compress1": {
                "Status": "m_true",
                "Alarm": "m_fo"
            },
            "compress2": {
                "Status": "m_true",
                "Alarm": "m_fo"
            },
            "compress3": {
                "Status": "m_true",
                "Alarm": "m_fo"
            }
        },
        "Machine": {
            "generator1": "m_true",
            "generator2": "",
            "generator3": "m_fo",
            "generator4": "m_true",
            "torch": "m_fo"
        }
    }
}

# PlcRemoteUse ___ init

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
