"""
    #: Default configuration parameters.
    default_config = ImmutableDict({
        'DEBUG':                                get_debug_flag(default=False),
        'TESTING':                              False,
        'PROPAGATE_EXCEPTIONS':                 None,
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    })
"""

import os

# root directory -> app.root_path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# code reload/debug online
ENV = 'develop'
DEBUG = True
SECRET_KEY = os.urandom(24)
SESSION_COOKIE_NAME = 'flask_session'

DATABASES = {
    'default': {
        'HOST': '',
        'ENGINE': 'sqlite3',
        'PORT': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    },
}

# BCRYPT_LOG_ROUNDS = 13
BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
DEBUG_TB_ENABLED = False  # Disable Debug toolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
# WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
