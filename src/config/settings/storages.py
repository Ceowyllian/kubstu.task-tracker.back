from datetime import timedelta

from config.env import env

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.staticfiles_storage",
    },
}

USE_MINIO = env.bool("USE_MINIO", False)
if USE_MINIO:
    MINIO_ENDPOINT = env.str("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = env.str("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = env.str("MINIO_SECRET_KEY")
    MINIO_USE_HTTPS = env.str("MINIO_USE_HTTPS", False)
    MINIO_URL_EXPIRY_HOURS = timedelta(hours=12)
    MINIO_CONSISTENCY_CHECK_ON_START = env.bool(
        "MINIO_CONSISTENCY_CHECK_ON_START", False
    )
    MINIO_BUCKET_CHECK_ON_SAVE = True
    MINIO_POLICY_HOOKS = []

    MINIO_PUBLIC_BUCKETS = [
        "django-backend-dev-public",
    ]
    MINIO_PRIVATE_BUCKETS = []
    STORAGES["default"]["BACKEND"] = "django_minio_backend.models.MinioBackend"
