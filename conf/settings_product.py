# -*- coding: utf-8 -*-
"""
    product settings
"""
ENV = 'product'
DEBUG = False
# ============================================
# database for product
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
