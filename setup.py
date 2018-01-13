#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2017, European Centre for Medium-Range Weather Forecasts (ECMWF).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


version = '0.0.1.dev0'


setuptools.setup(
    name='mpy',
    version=version,
    author='B-Open Solutions srl',
    author_email='info@bopen.eu',
    license='Apache License Version 2.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'cffi',
        'xarray',
    ],
    tests_require=[
        'pytest',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    keywords='',
    entry_points={
        'console_scripts': [
        ],
    },
)
