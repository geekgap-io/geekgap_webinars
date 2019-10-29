# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geekgap_webinars',
    version='1.0.0',
    description='Accompanying notebooks for GeekGap.io webinars',
    long_description=readme,
    author='Junior Teudjio Mbativou',
    author_email='junior.teudjio@geekgap.io',
    url='https://github.com/geekgap-io/geekgap_webinars',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

