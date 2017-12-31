from setuptools import setup, find_packages
from dice_plot import __VERSION__
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dice_plot',
    version='.'.join((str(v) for v in __VERSION__)),
    author='DICEhub',
    author_email='info@dicehub.com',
    description='DICE application tools',
    long_description=long_description,
    url='http://dicehub.com',
    packages = find_packages(),
    install_requires=[
        'dice_tools',
        'matplotlib',
        'lz4'
        ],
)
