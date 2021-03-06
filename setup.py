#!/usr/bin/env python
from setuptools import setup
from io import open

def readme():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()

setup(name='calculameBot',
      version='1.0',
      description='Python Telegram bot ',
      long_description=readme(),
      author='casave05',
      author_email='carlosmsv@gmail.com',
      url='https://github.com/casave5/calculamebot',
      #packages=['telebot'],
      license='GPL3',
      keywords='telegram bot ',
      #install_requires=['requests', 'six'],
      #extras_require={
      #    'json': 'ujson',
      #},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      ]
      )
