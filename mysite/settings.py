"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4vkv7x*xwadwo(aj7mpl#q*bbm=f*8@3pvgg3@1!#4c@ks$)uz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #  personal apps
    'news.apps.NewsConfig',
    'polls.apps.PollsConfig',
    'mysqldemo.apps.MysqldemoConfig',

    # third apps
    # "debug_toolbar",
    'import_export',
    # 'import_export_celery'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'author.middlewares.AuthorDefaultBackendMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '911222ab'
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
#  存放翻译文件的目录
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
# STATICFILES_DIRS = [
#     BASE_DIR / "static"
# ]
MEDIA_URL = "/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# simpleui 相关配置
# 首页配置
# SIMPLEUI_HOME_PAGE = 'http://127.0.0.1:8000/polls/'
# SIMPLEUI_HOME_TITLE = 'ZTZ后台管理' # 首页标题
# SIMPLEUI_HOME_ICON = 'fa fa-user' # 首页图标
SIMPLEUI_HOME_INFO = True  # 首页 服务器信息
SIMPLEUI_HOME_QUICK = True  # 首页 快捷操作
SIMPLEUI_ANALYSIS = False  # 统计信息 与否 默认上报一天一次
SIMPLEUI_DEFAULT_THEME = 'e-blue.css'  # 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_DEFAULT_ICON = True
SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['问卷调查', '权限认证', 'DEMO'],  # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': False,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
            'app': 'polls',
            'name': "问卷调查",
            'icon': 'fas fa-question-circle',
            'models': [
                {
                    'name': '问题',
                    'icon': 'fas fa-question-circle',
                    'url': 'polls/question'
                }, {
                    'name': '选项',
                    'icon': 'fas fa-question-circle',
                    'url': 'polls/choice'
                },
            ]
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                }, {
                    'name': '组',
                    'icon': 'fa fa-user',
                    'url': 'auth/group/'
                },
            ]
        },
        {
            'app': 'mysqldemo',
            'name': 'DEMO',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '职工',
                    'icon': 'fa fa-user',
                    'url': 'mysqldemo/employees/'
                }, {
                    'name': '客户',
                    'icon': 'fa fa-user',
                    'url': 'mysqldemo/customers/'
                },
            ]
        },

    ]
}

# import-export 相关配置
IMPORT_EXPORT_USE_TRANSACTIONS = True  # 资源导入是否应该使用数据库事务 默认是False
IMPORT_EXPORT_CHUNK_SIZE = 1024

# django-import-export-celery 相关配置
IMPORT_EXPORT_CELERY_INIT_MODULE = "mysite.celery"


def resource():  # Optional
    from polls.resource import QuestionResource
    return QuestionResource


IMPORT_EXPORT_CELERY_MODELS = {
    "Question": {
        'app_label': 'polls',
        'model_name': 'Question',
        # 'resource': resource,  # Optional
    }
}
