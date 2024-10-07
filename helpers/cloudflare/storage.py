from storages.backends.s3 import S3Storage

class StaticFileStorage(S3Storage):
    # helpers.cloudflare.storage.StaticFileStorage
    location = 'static'

class MediaFileStorage(S3Storage):
    # helpers.cloudflare.storage.MediaFileStorage
    location = 'media'