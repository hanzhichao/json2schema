#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))

version = '0.1.0'
setup_requirements = []
install_requires = []
tests_require = ['jsonschema', 'pytest']
extra_require = {'dev': tests_require + ['twine']}


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name='json2schema',
    version=version,
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='JSON to JSONSchema',
    license="MIT license",
    long_description=read_file('tests/README.md'),
    long_description_content_type="text/markdown",  # 新参数
    url='https://github.com/hanzhichao/json2schema',
    keywords=['json2schema', 'jsonschema', 'json to jsonschema'],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True,
    zip_safe=True,
    packages=find_packages(include=['json2schema']),

    setup_requires=setup_requirements,
    install_requires=install_requires,
    tests_require=tests_require,
    extra_require=extra_require,
)
