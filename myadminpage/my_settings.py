# Build paths inside the project like this: BASE_DIR / 'subdir'.
SECRET_KEY = 'django-insecure-ga1fr&e-t4%9f#*oxp66lz_l-#gy!2c-*5ib33wld-gfhw5-i9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exqressdb',
        'USER': 'admin',
        'PASSWORD': 'qwer1234',
        'HOST': 'exqress-rds.ctxktr2nwban.ap-northeast-2.rds.amazonaws.com',
        "PORT": 3306,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
