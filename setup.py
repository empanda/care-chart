#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='Care Chart',
    version='1.0',
    description="",
    author="Johannas Heller",
    author_email='johann+cc@phyfus.com',
    url='',
    packages=find_packages(),
    package_data={'care_chart': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
