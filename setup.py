"""placemaster python package configuration."""

from setuptools import setup

setup(
    name='placemaster',
    version='0.1.0',
    packages=['placemaster'],
    include_package_data=True,
    install_requires=[
        'authlib',
        'datetime',
        'flask',
        'flask_login',
        'flask_migrate',
        'flask_script',
        'flask_sqlalchemy',
        'html5validator',
        'google-api-python-client',
        'google-auth',
        'oauthlib',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pyOpenSSL',
        'psycopg2',
        'nodeenv',
        'requests',
        'requests_oauthlib',
        'sh',
        'selenium',
        'requests',
        'arrow'
    ],
)
