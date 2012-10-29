# Haystack settings for running tests.
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'fancy_tag_test.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fancy_tag_test.db'
    }
}

SECRET_KEY = 'mAtTzVPOV9JY4eJQfqgW8eAS9DWKnt3MkvvpQI2MzkhAz7z3'

INSTALLED_APPS = [
    'fancy_tag',
    'test_app',
]
