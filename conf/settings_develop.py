# -*- coding: utf-8 -*-
"""
    local settings
"""
ENV = 'develop'
# ============================================
# database for develop
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
