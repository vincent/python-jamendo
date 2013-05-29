#!/usr/bin/env python

import os
import sys

import jamendo

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'jamendo'
]

requires = [
    'requests'
]

setup(
    name='jamendo',
    version=jamendo.__version__,
    description='Python Jamendo API library.',
    long_description=open('README.md').read(),
    author='Vincent Lark',
    author_email='vincent.lark@gmail.com',
    url='http://github.com/vincent/python-jamendo',
    packages=packages,
    package_data={'': ['LICENSE'], 'jamendo': ['*.pem']},
    package_dir={'jamendo': 'jamendo'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
