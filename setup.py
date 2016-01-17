# -*- coding: utf-8 -*8-

from setuptools import setup
from setuptools import find_packages


setup(
    name='async-signal',
    packages=find_packages(),
    package_data={
        'async_signal': [],
    },
    version='0.1',
    description='Signals to use with asyncio',
    author='Tiago Lira',
    author_email='tiagoliradsantos@gmail.com',
    url='https://github.com/Tiago-Lira/async-signal',
    keywords=['asyncio', 'signals', 'python3', 'dispatch'],
    install_requires=[
        'asyncio>=3.4.3',
    ],
    zip_safe=False,
)
