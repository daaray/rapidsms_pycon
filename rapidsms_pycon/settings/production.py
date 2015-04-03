from rapidsms_pycon.settings.staging import *   # noqa

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'rapidsms_pycon_production'
DATABASES['default']['USER'] = 'rapidsms_pycon_production'

EMAIL_SUBJECT_PREFIX = '[Rapidsms_Pycon Prod] '

# Uncomment if using celery worker configuration
# BROKER_URL = 'amqp://rapidsms_pycon_production:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/rapidsms_pycon_production' % os.environ  # noqa