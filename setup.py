#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import version_info

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

ctx = {}

if version_info[0] < 3:
    execfile('tb-mqtt-client/_version.py', {}, ctx)
else:
    exec(compile(open('tb-mqtt-client/_version.py', "rb").read(), 'tb-mqtt-client/_version.py', 'exec'), {}, ctx)

setup(
    name = "tb-mqtt-client",
    version = ctx['__version__'],
    url = 'https://github.com/iscab-fr/thingsboard-python-client-sdk',
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['paho-mqtt'],
    author = "Thingsboard",
    author_email = "info@thingsboard.io",
    description = "ThingsBoard MQTT client Python SDK",
    license = "Apache Software License (Apache Software License 2.0)",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ]
)