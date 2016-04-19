from django.conf import settings

MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')
ADMIN_URL = getattr(settings, 'ADMIN_URL', '/admin/')
STATIC_URL = getattr(settings, 'STATIC_URL', '/static/')

# sbroumley 4/19/2016 - updated to dynamic setting:
# Authorization user model for django admin
AUTH_USER_MODEL = 'utility.AdminUser'
