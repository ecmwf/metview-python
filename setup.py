#!/usr/bin/env python3
#
# Copyright 2017-2019 B-Open Solutions srl.
# Copyright 2017-2019 European Centre for Medium-Range Weather Forecasts (ECMWF).
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


version = '1.2.0'


setuptools.setup(
    name='metview',
    version=version,
    description='Metview Python API.',
    long_description=read('README.rst'),
    author='European Centre for Medium-Range Weather Forecasts (ECMWF)',
    author_email='software.support@ecmwf.int',
    license='Apache License Version 2.0',
    url='https://github.com/ecmwf/metview-python',
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'cffi',
        'numpy',
        'pandas',
    ],
    tests_require=[
        'pytest',
    ],
    test_suite='tests',
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
)
