# -*- coding: utf-8 -*-
"""
    test settings
"""
ENV = 'test'
# ============================================
# database for test
# ============================================
DATABASES = {
    'default': {
        'HOST': 'localhost',
        'ENGINE': 'mysql',
        'PORT': 3306,
        'NAME': 'flask',
        'USER': 'root',
        'PASSWORD': 'root',
    },
}
