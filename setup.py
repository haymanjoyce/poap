from setuptools import setup, find_namespace_packages

setup(
    name='tool',
    version='0.1.0',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
        'colorama==0.4.6',
        'et-xmlfile==1.1.0',
        'numpy==1.26.2',
        'openpyxl==3.2.0b1',
        'pandas==2.1.3',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'setuptools==68.2.2',
        'six==1.16.0',
        'tzdata==2023.3',
    ],
    entry_points={
        'console_scripts': [
            'tool = src.tool.cli:cli',
        ],
    },
)

