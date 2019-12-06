"""placemaster python package configuration."""

from setuptools import setup

setup(
    name='placemaster',
    version='0.1.0',
    packages=['placemaster'],
    include_package_data=True,
    install_requires=[
        'datetime',
        'flask',
        'flask_login',
        'flask_sqlalchemy',
        'html5validator',
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
