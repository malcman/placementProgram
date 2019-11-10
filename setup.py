"""placemaster python package configuration."""

from setuptools import setup

setup(
    name='placemaster',
    version='0.1.0',
    packages=['placemaster'],
    include_package_data=True,
    install_requires=[
        'flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'nodeenv',
        'sh',
        'selenium',
        'requests',
        'arrow'
    ],
)
