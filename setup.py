#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-ujet',
      version='0.0.1',
      description='Singer.io tap for extracting data from the UJET API',
      author='jeff.huth@bytecode.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_ujet'],
      install_requires=[
          'backoff==1.8.0',
          'requests==2.22.0',
          'singer-python==5.8.1'
      ],
      entry_points='''
          [console_scripts]
          tap-ujet=tap_ujet:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_ujet': [
              'schemas/*.json',
              'tests/*.py'
          ]
      })
