from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# https://levelup.gitconnected.com/hosting-django-static-files-in-aws-using-s3-and-cloudfront-a-comprehensive-guide-2f8f5d0a845c


class StaticStorage(S3Boto3Storage):
    location = 'static'
    querystring_auth = False
    # Uncomment to use cloudfront
    # custom_domain = getattr(settings, 'AWS_CLOUDFRONT_DISTRIBUTION')


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    # custom_domain = getattr(settings, 'AWS_CLOUDFRONT_DISTRIBUTION')
