# -*- coding: utf-8 -*8-

from setuptools import setup
from setuptools import find_packages


setup(
    name='async-signal',
    packages=find_packages(),
    package_data={
        'async_signal': [],
    },
    version='0.1.1',
    description='Create signals to use with asyncio coroutines',
    author='Tiago Lira',
    author_email='tiagoliradsantos@gmail.com',
    url='https://github.com/Tiago-Lira/async-signal',
    download_url='https://github.com/Tiago-Lira/async-signal/tarball/0.1.1',
    keywords=[
        'asyncio',
        'signals',
        'python3',
        'dispatch',
        'async',
        'coroutines'
    ],
    install_requires=[
        'asyncio==3.4.3',
    ],
    zip_safe=False,
)
