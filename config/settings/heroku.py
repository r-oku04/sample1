import os
import dj_database_url

from .common import *

DEBUG = False
ALLOWED_HOSTS = ["*", ]

AWS_ACCESS_KEY_ID = "AKIAVFWILZP2USCRTTJZ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "kett"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL

DATABASES = {
    'default': dj_database_url.config()
}
