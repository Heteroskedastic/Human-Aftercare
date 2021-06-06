DEBUG = False

SECRET_KEY = '<SECRET_KEY>'

ALLOWED_HOSTS = ['*']

HOSTNAME = 'app.aftercareinternational.org'

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'human_aftercare',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'a',
    }
}

DEFAULT_FILE_STORAGE = 'human_aftercare.helpers.utils.S3MediaStorage'

AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY_ID>'
AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
AWS_STORAGE_BUCKET_NAME = 'human-aftercare-assets'
AWS_S3_REGION_NAME = 'nyc3'
AWS_S3_SIGNATURE_VERSION = 's3'
AWS_S3_ENDPOINT_URL = 'https://{}.digitaloceanspaces.com'.format(AWS_S3_REGION_NAME)
