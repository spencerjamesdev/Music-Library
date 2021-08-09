SECRET_KEY = 'django-insecure-$-f^^$!oixtoo#ryg_cby)#a01^6k*!+t@c%hec30ot9m4gz7u'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}