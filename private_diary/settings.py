import os#osモジュールを用いて、環境変数名を指定するため必要
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h05iir6jbarrw^-39af(4^)$jn8(5^xt%y%gowc6wj!-+s68*b"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "diary"#diaryというアプリケーションを作成したので追加する、diary/apps.pyにて確認することができる
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "private_diary.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "private_diary.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",#ENGINE→どのデータベース管理システムを使用するか表している（デフォルトでは、SQLite3になっている）→今回はPostgreSQLを使用するためこのように変更
        "NAME": "private_diary",#接続するデータベース名
        "USER": os.environ.get("DB_USER"),#PostgreSQLインストール時に自動生成されたスーパーユーザーを指定
        "PASSWORD" : os.environ.get("DB_PASSWORD"),#おなじく、パスワードを設定,あとで外部のサーバーと接続するため、直接記入してはいけない
        "HOST" : '',#ローカル環境のホスト（データベーす）に接続しようとしているため、空白
        "PORT" : '',#デフォルトのPostgreSQLに接続しようとしているため空白
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ja"#言語を日本語に設定

TIME_ZONE = "Asia/Tokyo"#タイムゾーンを日本に設定

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary ke"y field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#ロギングの設定、システムの動作やイベントの記録、監視
LOGGING = {#ログのメイン設定のディクショナリ
    "version": 1, #1固定
    "disable_exisiting_loggers" : False,#既存のロガーを無効にするか、今回の場合は、無視されない
    
    #ロガーの設定、ログのエントリーポイントの作成
    "loggers": {
        #Djangoが利用するロガー、Djangoのログを扱う
        "django": {
            "handlers": ["console"],#ログの出力先の設定
            "level": "INFO",#INFO→正常処理の記録
        },
        #diaryアプリケーションが利用するロガー
        "diary": {
            "handlers": ["console"],#ログの出力先の設定
            "level": "DEBUG",
        },
    },
    
    #ハンドれの設定、ログの出力先の設定
    "handlers": {
        "console": {
            "level": "DEBUG",#DEBUG→開発用のデバッグ用、プログラブの動作や振る舞いに関する問題やerror
            "class": "logging.StreamHandler",#StreamHandler→コンソールへ出力するハンドラ
            "formatter": "dev"#このハンドラで使用するフォーマッタの設定、以下で設定するformattersのクラス名
        },
    },
    
    #フォーマッタの設定、ログの出力形式の設定
    "formatters": {
        "dev": {
            "format": "\t".join([#フォーマットの設定、ログをタブ区切りで表示する方法
                "%(asctime)s",#ログエントリが作成された日時
                "[%(levelname)s]",#ログレベル(DEBUG,INFOなど)
                "%(pathname)s(Line:%(lineno)d)",#ログエントリを生成したファイルのパスと行番号
                "%(message)s"#ログメッセージ本体
            ])
        },
    } 
}