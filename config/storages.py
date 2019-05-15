from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
    'S3DefaultStorage',
)


# 정적 파일용
class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = settings.STATICFILES_LOCATION


# 미디어 파일용
class S3DefaultStorage(S3Boto3Storage):
    default_acl = 'private'
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False