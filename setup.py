#!/usr/bin/env python3
from setuptools import setup, find_packages

print("Setting up Environment for BOSCH-GLM-rangefinder")

setup(
    name='distance',
    version='0.0.1',
    author='patrickjoerg',
    author_email='patrickjoerg@gmx.ch',
    description='Tool for measuring distances.',
    url='https://github.com/petrisch/distance',
    install_requires=[
        'PyBluez==0.22',
        'requests==2.22.0',
        'pygi-composite-templates==0.2.4'
    ],
)
