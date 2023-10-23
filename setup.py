#! usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tool',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.3',
        'colorama==0.4.6',
        'numpy==1.24.3',
        'pandas==2.0.2',
        'python-dateutil==2.8.2',
        'pytz==2023.3',
        'six==1.16.0',
        'tzdata==2023.3',
    ],
    entry_points={
        'console_scripts': [
            'tool = src.tool',
        ],
    },
)

if __name__ == "__main__":
    setup()

