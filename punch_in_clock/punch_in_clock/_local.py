DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'punch_in_clock',
        'USER': 'vojin',
        'PASSWORD': 'lubenica',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = False

TIME_ZONE = 'Belgrade'

AUTH_USER_MODEL = 'punchInClock.User'
